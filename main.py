import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(300, 800))

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        item = fileMenu.Append(wx.ID_EXIT, "Еход\tCtrl+Q", "Еход высть!")

        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.onQuit, item)


    def onQuit(self, event):
        self.Close()

 
app = wx.App()

frame = MyFrame(None, "Fuck you again!")
frame.Show()

app.MainLoop()
