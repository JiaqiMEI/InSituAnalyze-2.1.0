#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.2 on Wed May  8 16:23:14 2019
#

import wx

import G

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((450, 180))
        self.panel_3 = wx.Panel(self, wx.ID_ANY)
        self.textLambda = wx.TextCtrl(self.panel_3, wx.ID_ANY, "100", style=wx.TE_CENTRE)
        self.textorder = wx.TextCtrl(self.panel_3, wx.ID_ANY, "1", style=wx.TE_CENTRE)
        self.textIter = wx.TextCtrl(self.panel_3, wx.ID_ANY, "15", style=wx.TE_CENTRE)
        self.ConfirmBtn = wx.Button(self.panel_3, wx.ID_ANY, "Confirm")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.ComfirmEve, self.ConfirmBtn)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("airPLS Baseline")
        self.textLambda.SetMinSize((60, -1))
        self.textorder.SetMinSize((60, -1))
        self.textIter.SetMinSize((60, -1))
        self.ConfirmBtn.SetMinSize((100, 30))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13.Add((20, 5), 0, 0, 0)
        label_1 = wx.StaticText(self.panel_3, wx.ID_ANY, "airPLS Baseline")
        sizer_13.Add(label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        sizer_13.Add((20, 5), 0, 0, 0)
        sizer_14.Add((10, 20), 1, wx.ALIGN_CENTER, 0)
        LambdaA = wx.StaticText(self.panel_3, wx.ID_ANY, "Lambda")
        sizer_14.Add(LambdaA, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer_14.Add(self.textLambda, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer_14.Add((10, 20), 1, 0, 0)
        orderA = wx.StaticText(self.panel_3, wx.ID_ANY, "Order")
        sizer_14.Add(orderA, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer_14.Add(self.textorder, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer_14.Add((10, 20), 1, wx.ALIGN_CENTER, 0)
        itermaxA = wx.StaticText(self.panel_3, wx.ID_ANY, "Iterations")
        sizer_14.Add(itermaxA, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer_14.Add(self.textIter, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        sizer_14.Add((10, 20), 1, wx.ALIGN_CENTER, 0)
        sizer_13.Add(sizer_14, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_13.Add((20, 5), 0, 0, 0)
        sizer_15.Add((175, 5), 1, 0, 0)
        sizer_15.Add(self.ConfirmBtn, 0, wx.ALL, 5)
        sizer_15.Add((175, 5), 1, 0, 0)
        sizer_13.Add(sizer_15, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        self.panel_3.SetSizer(sizer_13)
        sizer_12.Add(self.panel_3, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_12)
        self.Layout()
        # end wxGlade

    def ConfirmEve(self, event):  # wxGlade: MyFrame.<event_handler>
        #print("Event handler 'ComfirmEve' not implemented!")
        #event.Skip()

        G.BaselineLambda = float(self.textLambda.GetValue())
        G.BaselineOrder = int(self.textorder.GetValue())
        G.BaselineIter = int(self.textIter.GetValue())

        self.Destroy()

# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
