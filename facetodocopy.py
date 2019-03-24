import wx
import todoistcopy

import wx

APP_EXIT = 1
APP_EDIT = 2


class Example(wx.Frame):
    panelTask = None
    panelProject = None


    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        panelbut = wx.Panel(self, wx.ID_ANY, size=(100, 150), pos = (10, 10))
        self.panelTask = wx.Panel(self, wx.ID_ANY, size=(340, 100), pos = (80, 10))
        self.panelProject = wx.Panel(self, wx.ID_ANY, size=(340, 100), pos=(80, 10))
        wx.TextCtrl(self.panelTask, wx.ID_ANY, "Zadachi", size=(350, 100), pos = (80, 10))
        wx.TextCtrl(self.panelProject, wx.ID_ANY, "Project", size=(350, 100), pos=(80, 10))

        button1 = wx.Button(panelbut, label="Задачи", pos=(10, 10), size=(70, 50))
        button2 = wx.Button(panelbut, label="Проекты", pos=(10, 60), size=(70, 50))
        self.Bind(wx.EVT_BUTTON, self.showTask, button1)
        self.Bind(wx.EVT_BUTTON, self.showProject, button2)

        self.SetSize((450, 450))
        self.SetTitle('Todocopy')
        self.Centre()
        self.panelProject.Hide()

    def showTask(self,event):
        self.panelTask.Show()
        self.panelProject.Hide()

    def showProject(self,event):
        self.panelTask.Hide()
        self.panelProject.Show()

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()