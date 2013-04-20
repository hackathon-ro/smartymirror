import time
import wx
import wx.gizmos as gizmos
class LED_clock(wx.Frame):
    def __init__(self, parent, id):
        pos = wx.DefaultPosition
        wx.Frame.__init__(self, parent, id, title='Clock', pos=pos, size=(600, 100))
        size = wx.DefaultSize
        style = gizmos.LED_ALIGN_CENTER
        self.led = gizmos.LEDNumberCtrl(self, -1, pos, (20, 20), style)
        # culori de folosit
        self.led.SetBackgroundColour("black")
        self.led.SetForegroundColour("cyan")
        self.OnTimer(None)
        self.timer = wx.Timer(self, -1)
        # update clock digits every second (1000ms)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.Centre()
    def OnTimer(self, event):
        # timpul curent
        current = time.localtime(time.time())
        # formatare ceas
        ts = time.strftime("%H %M %S", current)
        self.led.SetValue(ts)
# testare
if __name__ == '__main__':
    app = wx.App()
    frame = LED_clock(None, -1)
    frame.Show(True)
    app.SetTopWindow(frame)
    app.MainLoop()
