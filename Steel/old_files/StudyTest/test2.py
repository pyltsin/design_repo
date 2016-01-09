# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 00:02:51 2014

@author: Pyltsin
"""

# -*- coding: cp1251 -*-
import win32com.client
objWord = win32com.client.Dispatch(r'Word.Application',"Администратор",UnicodeToString="cp1251")
objWord.Visible = True
objDoc = objWord.Documents.Add()
objDoc.Activate
objDoc.ActiveWindow.Selection.InsertAfter("Привет.")
objDoc.ActiveWindow.Selection.InsertParagraphAfter
objDoc.ActiveWindow.Selection.InsertAfter("Чувачёк.")
objDoc.ActiveWindow.Selection.InsertParagraphAfter
objDoc.ActiveWindow.Selection.Font.Bold = True
objDoc.ActiveWindow.Selection.EndOf
#objDoc.SaveAs("C:/Test.doc")
del objDocs
objWord.Quit()


Sub Ìàêðîñ1()
'
' Ìàêðîñ1 Ìàêðîñ
'
'
    Selection.MoveRight Unit:=wdCharacter, Count:=14
    Selection.TypeParagraph
    Selection.Font.Bold = wdToggle
    Application.Keyboard (1049)
    Selection.TypeText Text:="Ðàñ÷åò ñå÷åíèÿ"
End Sub
Sub Ìàêðîñ2()
'
' Ìàêðîñ2 Ìàêðîñ
'
'
    Application.Keyboard (1049)
    Selection.TypeText Text:="Ïðèâåò"
    Selection.TypeParagraph
    Selection.TypeText Text:="Ýòî ìàêðîñ"
    Selection.TypeParagraph
    Selection.TypeText Text:="Ïðèâåò"
    Selection.TypeParagraph
    Selection.Style = ActiveDocument.Styles("Çàãîëîâîê 1")
    Selection.TypeText Text:="Ïðèâåò"
End Sub
Sub Ìàêðîñ3()
'
' Ìàêðîñ3 Ìàêðîñ
'
'
    Selection.TypeParagraph
    Selection.Style = ActiveDocument.Styles("Îáû÷íûé")
    Selection.Font.Bold = wdToggle
    Selection.TypeText Text:="Hfcxtn ctxtybz"
    Selection.TypeParagraph
    Selection.Font.Bold = wdToggle
    Selection.TypeText Text:="Nbg ctxtybz^ ldenfdh"
    Selection.TypeParagraph
    Selection.InlineShapes.AddPicture FileName:= _
        "D:\python_my\Construct\SortamentPicture\dvut.png", LinkToFile:=False, _
        SaveWithDocument:=True
End Sub