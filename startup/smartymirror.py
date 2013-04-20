#!/usr/bin/python

import wx
import wx.lib.buttons as buttons
import os
 
class MyForm(wx.Frame):
 
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Mirror Apps", size=(200,200))
        panel = wx.Panel(self, wx.ID_ANY)
        panel.SetBackgroundColour("black")
	panel.Refresh()
 
        # create a normal toggle button
        button_horoscop = wx.Button(panel, label="Horoscop")
        button_horoscop.Bind(wx.EVT_BUTTON, self.onHoroscop)

        button_vremea = wx.Button(panel, label="Vremea")
        button_vremea.Bind(wx.EVT_BUTTON, self.onVremea)
         
        button_clock = wx.Button(panel, label="Clock")
        button_clock.Bind(wx.EVT_BUTTON, self.onClock)

        button_quote = wx.Button(panel, label="Quote of the day")
        button_quote.Bind(wx.EVT_BUTTON, self.onQuote)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(button_horoscop, 0, wx.ALL, 5)
        sizer.Add(button_vremea, 0, wx.ALL, 5)
        sizer.Add(button_clock, 0, wx.ALL, 5)
        sizer.Add(button_quote, 0, wx.ALL, 5)

        panel.SetSizer(sizer)
 
    #----------------------------------------------------------------------

    def onHoroscop(self,eventq):
	revalue = os.system("python /home/pi/smartmirror/apps/horoscope/horoscope.py &")	

    def onVremea(self,eventq):
	revalue = os.system("python /home/pi/smartmirror/apps/weather/weather.py &")

    def onClock(self,eventq):
        revalue = os.system("python /home/pi/smartmirror/apps/clock/clock.py &")

    def onQuote(self,eventq):
	revalue = os.system("/home/pi/smartmirror/apps/quote/quote.sh")


    #----------------------------------------------------------------------
 
 
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
