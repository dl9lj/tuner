#dl9lj 2023 
#script for Yaesu FC-1000	
#Arduino Uno with RF24 connected to USB (TX)

#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import serial
import socket
#import time
from array import *

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=2)
# ser.open()
# ser.write("C255;0;0")
# ser.close()

class Example(wx.Frame):
           
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        self.InitUI()
        
    def InitUI(self):   
            
        pnl = wx.Panel(self)
        self.a = wx.StaticText(pnl, label='Relais', pos=(20, 10))  
        self.a = wx.StaticText(pnl, label='RL1', pos=(20, 30))  
        self.a = wx.StaticText(pnl, label='RL3', pos=(60, 30))  
        self.a = wx.StaticText(pnl, label='RL4', pos=(100, 30))  
        
        self.ra1 = wx.RadioButton(pnl,  pos=(20, 50), 
            style=wx.RB_GROUP)
        self.ra2 = wx.RadioButton(pnl,  pos=(20, 70))
        self.ra1.Bind(wx.EVT_RADIOBUTTON, self.OnPointA)
        self.ra2.Bind(wx.EVT_RADIOBUTTON, self.OnPointA)

        self.rb1 = wx.RadioButton(pnl,  pos=(60, 50), 
            style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(pnl,  pos=(60, 70))
        self.rb1.Bind(wx.EVT_RADIOBUTTON, self.OnPointB)
        self.rb2.Bind(wx.EVT_RADIOBUTTON, self.OnPointB)

        self.rc1 = wx.RadioButton(pnl,  pos=(100, 50), 
            style=wx.RB_GROUP)
        self.rc2 = wx.RadioButton(pnl,  pos=(100, 70))
        self.rc1.Bind(wx.EVT_RADIOBUTTON, self.OnPointC)
        self.rc2.Bind(wx.EVT_RADIOBUTTON, self.OnPointC)

      


        slda = wx.Slider(pnl, value=0, minValue=0, maxValue=127, pos=(100, 120), 
            size=(250, -1), style=wx.SL_HORIZONTAL)
            
        slda.Bind(wx.EVT_SCROLL, self.OnSliderScrollA)
            
        sldb = wx.Slider(pnl, value=0, minValue=0, maxValue=63, pos=(100, 150), 
            size=(250, -1), style=wx.SL_HORIZONTAL)    
        
        sldb.Bind(wx.EVT_SCROLL, self.OnSliderScrollB)

        sldc = wx.Slider(pnl, value=0, minValue=0, maxValue=31, pos=(100, 180), 
            size=(250, -1), style=wx.SL_HORIZONTAL)    
        
        sldc.Bind(wx.EVT_SCROLL, self.OnSliderScrollC)        

        self.rr1 = wx.RadioButton(pnl, label='A off', pos=(400, 120), 
            style=wx.RB_GROUP)
        self.rr1.Bind(wx.EVT_RADIOBUTTON, self.OnPointR1)
        
        self.rr2 = wx.RadioButton(pnl, label='B off', pos=(400, 150),
			style=wx.RB_GROUP)
        self.rr2.Bind(wx.EVT_RADIOBUTTON, self.OnPointR2)

        self.rr3 = wx.RadioButton(pnl, label='C off', pos=(400, 180),
			style=wx.RB_GROUP)
        self.rr3.Bind(wx.EVT_RADIOBUTTON, self.OnPointR3)


        self.rr4 = wx.RadioButton(pnl, label='AllOff', pos=(400, 50),
			style=wx.RB_GROUP)
        self.rr4.Bind(wx.EVT_RADIOBUTTON, self.OnPointR4)

        self.rr5 = wx.RadioButton(pnl, label='THRU', pos=(400, 80),
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

        self.rr9 = wx.RadioButton(pnl, label='10m', pos=(400, 330),
			style=wx.RB_GROUP)
        self.rr9.Bind(wx.EVT_RADIOBUTTON, self.OnPointR9)
                
        self.SetSize((510, 400))
        self.SetTitle('Antenna Tuner Yaesu FC-800 RF24')
        self.Centre()
        self.Show(True)     

        
    def OnPointA(self, e):
        if self.ra1.GetValue(): val = 128
        if self.ra2.GetValue(): val = 0
        #print val
        self.g = val
        self.Tune()
        
    def OnPointB(self, e):
        if self.rb1.GetValue(): val = 128
        if self.rb2.GetValue(): val = 0
        #print val
        self.h = val
        self.Tune()
        
    def OnPointC(self, e):
        if self.rc1.GetValue(): val = 64
        if self.rc2.GetValue(): val = 0
        #print val
        self.i = val
        self.Tune()



    def OnSliderScrollA(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        #val = val + 128
        #val = LUT[val]
        #val = val >> 1
        val = val + 1000
        #print val
        self.d = val
        self.Tune()


    def OnSliderScrollB(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        val = val + 2000
        #print val
        self.e = val
        self.Tune()


    def OnSliderScrollC(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        val = val + 3000
        #print val
        self.f = val
        self.Tune()

    def OnPointR1(self, e):
        if self.rr1.GetValue(): val = 1000
        #print val
        self.d = val
        self.Tune()

    def OnPointR2(self, e):
        if self.rr2.GetValue(): val = 2000
        #print val
        self.e = val
        self.Tune()

    def OnPointR3(self, e):
        if self.rr3.GetValue(): val = 3000
        #print val
        self.f = val
        self.Tune()

    def OnPointR4(self, e):
        self.d = 1000
        self.e = 2000
        self.f = 3000
        self.g = 0
        self.h = 0
        self.i = 0
        self.k = 0
        self.l = 0
        self.j = 0
        self.Tune()

    def OnPointR5(self, e):
        self.d = 1255
        self.e = 2255
        self.f = 3255
        self.g = 0
        self.h = 0
        self.i = 0
        self.Tune()

    def OnPointR6(self, e):
        self.k = 1031
        self.l = 2156
        self.j = 3026
        self.Update()

    def OnPointR7(self, e):
        self.k = 1034
        self.l = 2170
        self.j = 3031
        self.Update()

    def OnPointR8(self, e):
        self.k = 1012
        self.l = 2121
        self.j = 3011
        self.Update()

    def OnPointR9(self, e):
        self.k = 1000
        self.l = 2000
        self.j = 3031
        self.Update()

	
    def Update(self):
        self.k = str(self.k)
        print(self.k.encode('ascii'))
        ser.write(self.k.encode('ascii'))
        self.l = str(self.l)
        print(self.l.encode('ascii'))
        ser.write(self.l.encode('ascii'))
        self.j = str(self.j)
        print(self.j.encode('ascii'))
        ser.write(self.j.encode('ascii'))
        
    def Tune(self):
        self.k = self.d + self.g
        self.l = self.e + self.h + self.i
        self.j = str(self.k)
        print(self.j.encode('ascii'))
        ser.write(self.j.encode('ascii'))
        self.j = str(self.l)
        print(self.j.encode('ascii'))
        ser.write(self.j.encode('ascii'))
        self.j = str(self.f)
        print(self.j.encode('ascii'))
        ser.write(self.j.encode('ascii'))
        
LUT = [0, 32, 16, 48, 8, 40, 24, 56, 4, 36, 20, 52, 12, 44, 28, 60, 
       2, 34, 18, 50, 10, 42, 26, 58, 6, 38, 22, 54, 14, 46, 30, 62,
       1, 33, 17, 49, 9, 41, 25, 57, 5, 37, 21, 53, 13, 45, 29, 61, 
       3, 35, 19, 51, 11, 43, 27, 59, 7, 39, 23, 55, 15, 47, 31, 63,
       128, 160, 144, 176, 136, 168, 152, 184, 132, 164, 148, 180, 140, 172, 156, 188,
       130, 162, 146, 178, 138, 170, 154, 186, 134, 166, 150, 182, 142, 174, 158, 190,    
       129, 161, 145, 177, 137, 169, 153, 185, 133, 165, 149, 181, 141, 173, 157, 189, 
       131, 163, 147, 179, 139, 171, 155, 187, 135, 167, 151, 183, 143, 175, 159, 191]   

def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    

if __name__ == '__main__':
      main()   
