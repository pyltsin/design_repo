# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:50:17 2013

@author: puma
"""

class lists():
    def __init__(self, filename):
        self.filename=filename
        self.infile = open(filename, 'r')
        self.filestr = self.infile.read()
        #print(self.filestr)
        self.words = self.filestr.split()
        #print(self.words)
        self.infile.close()
        self.lenght=len(self.words)
    def get_words(self):
        return self.words
    def get_word(self, n):
        return self.words[n]
    def get_lenght(self):
        return self.lenght
    def get_filename(self):
        return self.filename
        
class tables_csv():
    def __init__(self, filename, typ='none'):
        self.filename=filename
#        print filename
        self.infile = open(filename, 'r')
        import csv
        self.table = []
        for row in csv.reader(self.infile):
#            print row
            self.table.append(row)
        self.infile.close()
        self.typ=typ
        if self.typ=='float':
            for r in range(1,len(self.table)):
                for c in range(1, len(self.table[0])):
#                    print self.table[r][c]
                    self.table[r][c] =  float(self.table[r][c])
        if self.typ=='float_all':
            for r in range(0,len(self.table)):
                for c in range(0, len(self.table[0])):
#                    print self.table[r][c]
                    self.table[r][c] =  float(self.table[r][c])
#                    print self.table[r][c]
        if self.typ!='float_all':

            for x in self.table:
    
                x[0]=unicode(x[0], 'utf-8')
    #            x[0]=x[0].replace('Y', u'У')
    #            x[0]=x[0].replace('II', u'П')
    def get_table(self):
        return self.table
    def get_lenght_column(self):
        return len(self.table)
    def get_lenght_row(self):
        return len(self.table[0])
    def get_ij(self, i, j):
        return self.table[i][j]
    def get_title_row(self, n=1):
        return self.table[0][n:]
    def get_title_column(self, n=1):
        title_column=[]
        for n in range(n,len(self.table)):
            title_column.append(self.table[n][0])
        return title_column
    def get_filename(self):
        return self.filename
    def get_cell(self, name_x, name_y):
        cell=False
        for r in range(1,len(self.table)):
            for c in range(1, len(self.table[0])):
                if name_x==self.table[0][c] and name_y==self.table[r][0]:
                    cell=self.table[r][c]
        return cell
    def get_interpolate(self,x, y):
        if self.typ=='float_all':
            x1=False
            x2=False
            y1=False
            y2=False
            for i in range(1, self.get_lenght_row()):
                if x>=self.table[0][i-1] and x<=self.table[0][i]:
                    x1=i-1
                    x2=i
#                    print x1, x2
 
            for i in range(1, self.get_lenght_column()):
                if y>=self.table[i-1][0] and y<=self.table[i][0]:
                    y1=i-1
                    y2=i
#                   print y1, y2
        
            if x1==False or y1==False or x2==False or y2==False:
                return False  
        
            else:
                cell1=(self.get_ij(y1,x2)-self.get_ij(y1,x1))\
                /(self.get_ij(0,x2)-self.get_ij(0,x1))*(x-self.get_ij(0,x1))\
                +self.get_ij(y1,x1)
              
                cell2=(self.get_ij(y2,x2)-self.get_ij(y2,x1))\
                /(self.get_ij(0,x2)-self.get_ij(0,x1))*(x-self.get_ij(0,x1))\
                +self.get_ij(y2,x1)
                
                cell=(cell2-cell1)/(self.get_ij(y2,0)-self.get_ij(y1,0))*\
                (y-self.get_ij(y1,0))+cell1               
                return cell
        else:
            return False    
        




