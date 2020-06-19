import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(300, 800))

        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        runMenu = wx.Menu()

        fileMenu.Append(100, "&Open\tCtrl+O", "Open file...")
        fileMenu.Append(103, "&Start\tCtrl+S", "Run build")
        fileMenu.AppendSeparator() 
        item = wx.MenuItem(fileMenu, 101, "&Exit\tCtrl+Q", "Еход высть!")
        fileMenu.Append(item)

        runMenu.Append(102, "Start buildorder", "Start buildorder", kind=wx.ITEM_RADIO)
        runMenu.Append(104, "Start buildorder", "Pause buildorder", kind=wx.ITEM_RADIO)

        menubar.Append(fileMenu, "&File")
        menubar.Append(runMenu, "&Run")

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.onOpen,  id=100)
        self.Bind(wx.EVT_MENU, self.onQuit,  id=101)
        self.Bind(wx.EVT_MENU, self.onRun,   id=102)
        self.Bind(wx.EVT_MENU, self.onStart, id=103)

        panel = wx.Panel(self)
        vbox = wx.BoxSizer()

        mp = wx.Panel(panel)
        mp.SetBackgroundColour('#ff99e6')

        vbox.Add(mp, wx.ID_ANY, wx.EXPAND | wx.ALL, 10)

        panel.SetSizer(vbox)

    def onQuit(self, event):
        self.Close()


    def onOpen(self, event):
        print("Opened")


    def onRun(self, event):
        print("Run timer and start angry sounds")


    def onStart(self, event):
        pass

 
app = wx.App()

frame = MyFrame(None, "Fuck you again!")
frame.Show()

app.MainLoop()
