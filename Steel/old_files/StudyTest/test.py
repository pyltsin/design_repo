import win32com.client

wordapp = win32com.client.Dispatch("Word.Application") 
wordapp.Visible = 1 
worddoc = wordapp.Documents.Add()
worddoc.PageSetup.Orientation = 1 
worddoc.PageSetup.BookFoldPrinting = 1 
worddoc.Content.Font.Size = 11
worddoc.Content.Paragraphs.TabStops.Add (100)
worddoc.Content.Text = "Hello, I am a text!"

location = worddoc.Range()
location.Paragraphs.Add()
location.Collapse(0)
location.Paragraphs.Add()
location.Collapse(1)
table = location.Tables.Add (location, 3, 4)
table.ApplyStyleHeadingRows = 1
table.AutoFormat(16)
table.Cell(1,1).Range.InsertAfter("Teacher")

location1 = worddoc.Range()
location1.Paragraphs.Add()
location1.Collapse(1)
table = location1.Tables.Add (location1, 3, 4)
table.ApplyStyleHeadingRows = 1
table.AutoFormat(16)
table.Cell(1,1).Range.InsertAfter("Teacher1")
worddoc.Content.MoveEnd

worddoc.ActiveWindow.Selection.InlineShapes.AddPicture('D:\python_my\Construct\SortamentPicture/shvel.png')
#worddoc.Close() # Close the Word Document (a save-Dialog pops up)
#wordapp.Quit() # Close the Word Application
del wordapp