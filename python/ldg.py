#dl9lj 2023 
#script for LDG AT-1000	
#Arduino Uno with RF24 connected to USB (TX)

#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import serial
import socket
# import time
from array import *

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2)

class Example(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        self.InitUI()
        
    def InitUI(self):   
            
        pnl = wx.Panel(self)
        
        slda = wx.Slider(pnl, value=0, minValue=0, maxValue=127, pos=(100, 120), 
            size=(250, -1), style=wx.SL_HORIZONTAL)

        slda.Bind(wx.EVT_SCROLL, self.OnSliderScrollA)
            
        sldb = wx.Slider(pnl, value=0, minValue=0, maxValue=127, pos=(100, 150), 
            size=(250, -1), style=wx.SL_HORIZONTAL)    
        
        sldb.Bind(wx.EVT_SCROLL, self.OnSliderScrollB)
        
        text1 = wx.StaticText(pnl, label='CAP', pos=(60, 125))
        text2 = wx.StaticText(pnl, label='IND', pos=(60, 155))
        
        self.rr1 = wx.RadioButton(pnl, label='A off', pos=(400, 120), 
            style=wx.RB_GROUP)
        self.rr1.Bind(wx.EVT_RADIOBUTTON, self.OnPointR1)
        
        self.rr2 = wx.RadioButton(pnl, label='B off', pos=(400, 150),
			style=wx.RB_GROUP)
        self.rr2.Bind(wx.EVT_RADIOBUTTON, self.OnPointR2)

        self.rr4 = wx.RadioButton(pnl, label='Thru', pos=(400, 50),
			style=wx.RB_GROUP)
        self.rr4.Bind(wx.EVT_RADIOBUTTON, self.OnPointR4)

        self.rr5 = wx.RadioButton(pnl, label='AllOn', pos=(400, 80),
			style=wx.RB_GROUP)
        self.rr5.Bind(wx.EVT_RADIOBUTTON, self.OnPointR5)

        self.rr6 = wx.RadioButton(pnl, label='80m', pos=(400, 240),
			style=wx.RB_GROUP)
        self.rr6.Bind(wx.EVT_RADIOBUTTON, self.OnPointR6)

        self.rr7 = wx.RadioButton(pnl, label='40m', pos=(400, 270),
			style=wx.RB_GROUP)
        self.rr7.Bind(wx.EVT_RADIOBUTTON, self.OnPointR7)

        self.rr8 = wx.RadioButton(pnl, label='20m', pos=(400, 300),
			style=wx.RB_GROUP)
        self.rr8.Bind(wx.EVT_RADIOBUTTON, self.OnPointR8)

        self.rr9 = wx.RadioButton(pnl, label='15m', pos=(400, 330),
			style=wx.RB_GROUP)
        self.rr9.Bind(wx.EVT_RADIOBUTTON, self.OnPointR9)
            
        self.SetSize((510, 400))
        self.SetTitle('Antenna Tuner LDG AT-1000 RF24')
        self.Centre()
        self.Show(True)     

    def OnSliderScrollA(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        val = val + 1000
        #print val
        self.k = val
        self.Update()

    def OnSliderScrollB(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        val = val + 2000
        #print val
        self.l = val
        self.Update()

    def OnPointR1(self, e):
        if self.rr1.GetValue(): val = 1000
        #print val
        self.k = val
        self.Update()

    def OnPointR2(self, e):
        if self.rr2.GetValue(): val = 2000
        #print val
        self.l = val
        self.Update()

    def OnPointR4(self, e):
        self.k = 1000
        self.l = 2000
        self.Update()

    def OnPointR5(self, e):
        self.k = 1255
        self.l = 2255
        self.Update()

    def OnPointR6(self, e):
        self.k = 1022
        self.l = 2127
        self.Update()

    def OnPointR7(self, e):
        self.k = 1000
        self.l = 2051
        self.Update()

    def OnPointR8(self, e):
        self.k = 1000
        self.l = 2015
        self.Update()

    def OnPointR9(self, e):
        self.k = 1000
        self.l = 2013
        self.Update()
	
    def Update(self):
        self.k = str(self.k)
        print(self.k.encode('ascii'))
        ser.write(self.k.encode('ascii'))
        #time.sleep(0.5)
        self.l = str(self.l)
        print(self.l.encode('ascii'))
        ser.write(self.l.encode('ascii'))
        #time.sleep(0.2)
        
def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    

if __name__ == '__main__':
      main()   
