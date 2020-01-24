#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.2 on Fri May 10 12:54:43 2019
#

import wx
import numpy as np
import cv2
import G
import GS

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: GRPurge.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((750, 750))
        self.Panel1 = wx.Panel(self, wx.ID_ANY)
        self.Panel = wx.Panel(self.Panel1, wx.ID_ANY)
        figure = self.matplotlib_figure = Figure()
        self.matplotlib_axes = figure.add_subplot(111)  # 1x1 grid, first subplot
        self.Figure = FigureCanvas(self.Panel, wx.ID_ANY, figure)
        self.captureBtn = wx.Button(self.Panel1, wx.ID_ANY, "Capture")
        self.zeroBtn = wx.Button(self.Panel1, wx.ID_ANY, "Zeroing")
        self.erodeBtn = wx.Button(self.Panel1, wx.ID_ANY, "Erode")
        self.dilateBtn = wx.Button(self.Panel1, wx.ID_ANY, "Dilate")
        self.resetBtn = wx.Button(self.Panel1, wx.ID_ANY, "Reset")
        self.confirmBtn = wx.Button(self.Panel1, wx.ID_ANY, "Confirm")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.captureEve, self.captureBtn)
        self.Bind(wx.EVT_BUTTON, self.zeroEve, self.zeroBtn)
        self.Bind(wx.EVT_BUTTON, self.erodeEve, self.erodeBtn)
        self.Bind(wx.EVT_BUTTON, self.dilateEve, self.dilateBtn)
        self.Bind(wx.EVT_BUTTON, self.resetEve, self.resetBtn)
        self.Bind(wx.EVT_BUTTON, self.confirmEve, self.confirmBtn)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: GRPurge.__set_properties
        self.SetTitle("Purge")
        self.Figure.SetMinSize((500, 700))
        self.Panel.SetMinSize((500, 700))
        self.captureBtn.SetMinSize((200, 60))
        self.zeroBtn.SetMinSize((200, 60))
        self.erodeBtn.SetMinSize((200, 60))
        self.dilateBtn.SetMinSize((200, 60))
        self.resetBtn.SetMinSize((200, 60))
        self.confirmBtn.SetMinSize((200, 60))
        self.Panel1.SetMinSize((720, 720))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: GRPurge.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.Figure, 1, wx.EXPAND, 0)
        self.Panel.SetSizer(sizer_4)
        sizer_2.Add(self.Panel, 1, wx.EXPAND, 0)
        sizer_3.Add((20, 160), 0, 0, 0)
        sizer_3.Add(self.captureBtn, 0, wx.ALL, 5)
        sizer_3.Add(self.zeroBtn, 0, wx.ALL, 5)
        sizer_3.Add(self.erodeBtn, 0, wx.ALL, 5)
        sizer_3.Add(self.dilateBtn, 0, wx.ALL, 5)
        sizer_3.Add(self.resetBtn, 0, wx.ALL, 5)
        sizer_3.Add((20, 100), 0, 0, 0)
        sizer_3.Add(self.confirmBtn, 0, wx.ALL, 5)
        sizer_3.Add((20, 160), 0, 0, 0)
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)
        self.Panel1.SetSizer(sizer_2)
        sizer_1.Add(self.Panel1, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def setParent(self, parent, parentName, data, figure, axes, cmap, textCtrl):
        print(parent)
        self.parent = parent
        self.parent.Name = parentName
        self.parent.Data = data
        self.parent.Axes = axes
        self.parent.Figure = figure
        self.parent.cmap = cmap
        try:
            self.parent.textCtrl = textCtrl
        except:
            pass

        global Purge
        Purge = np.copy(data)

    def captureEve(self, event):  # wxGlade: GRPurge.<event_handler>
        #print("Event handler 'captureEve' not implemented!")
        #event.Skip()

        # 本文件内绘图均使用Purge，重置(reset)时用对Purge重新赋值为self.parent.Data

        # 绑定鼠标事件
        self.Figure.mpl_connect('button_press_event', self.onPress)
        self.Figure.mpl_connect('button_release_event', self.onMove)
        # self.Figure.mpl_connect('motion_notify_event', self.onRelease)
        # self.Figure.mpl_connect('scroll_event', self.onScroll)

    # 捕获鼠标事件
    def onPress(self, event):
        # 大段注释部分为选择多点的考虑，但多边形置零区域不太会
        # print('my position:', event.button, event.xdata, event.ydata)
        # 定义全局变量，仅在本文件内使用
        global pt
        global Purge
        m, n = np.shape(GS.fore)

        if event.inaxes != None:
            x = int(event.xdata)
            y = int(event.ydata)
            # 控制值域
            if x == n - 1:
                x = n
            if y == m - 1:
                y = m
            # 取值
            pt = (x, y)

            # 清除axes中的绘图痕迹
            self.matplotlib_axes.cla()
            # 重绘
            self.matplotlib_axes.imshow(Purge, cmap=self.parent.cmap)
            self.matplotlib_axes.set_xticks([])
            self.matplotlib_axes.set_yticks([])

            # 绘图的基础上加点和直线
            self.matplotlib_axes.scatter(int(x), int(y), s=2.5, color='red')
            self.Figure.draw()

    def onMove(self, event):
        global pt
        global pt2
        # global Purge
        m, n = np.shape(GS.fore)

        if event.inaxes != None:
            x = int(event.xdata)
            y = int(event.ydata)
            # 控制值域
            if x == n - 1:
                x = n
            if y == m - 1:
                y = m
            # 取值，计数+1
            pt2 = (x, y)

            # 绘图的基础上加点和直线
            self.matplotlib_axes.scatter(int(x), int(y), s=2.5, color='red')
            # self.matplotlib_axes.plot([pt[0], pt2[0]],[pt[1], pt2[1]], 'k--', lw=1, color='red')
            self.matplotlib_axes.plot([pt[0], pt2[0]], [pt[1], pt[1]], 'k--', lw=1, color='red')
            self.matplotlib_axes.plot([pt[0], pt[0]], [pt[1], pt2[1]], 'k--', lw=1, color='red')
            self.matplotlib_axes.plot([pt[0], pt2[0]], [pt2[1], pt2[1]], 'k--', lw=1, color='red')
            self.matplotlib_axes.plot([pt2[0], pt2[0]], [pt[1], pt2[1]], 'k--', lw=1, color='red')

            self.Figure.draw()

    def onRelease(self, event):
        pass

    def onScroll(self, event):
        pass

    def zeroEve(self, event):  # wxGlade: GRPurge.<event_handler>
        #print("Event handler 'zeroEve' not implemented!")
        #event.Skip()
        global pt
        global pt2
        global Purge
        # 选定区域置零
        Purge[pt[1]:pt2[1], pt[0]:pt2[0]] = 0
        # 清除axes中的绘图痕迹
        self.matplotlib_axes.cla()
        # 重绘
        self.matplotlib_axes.imshow(Purge, cmap=self.parent.cmap)
        self.matplotlib_axes.set_xticks([])
        self.matplotlib_axes.set_yticks([])
        self.Figure.draw()


    def erodeEve(self, event):  # wxGlade: GRPurge.<event_handler>
        #print("Event handler 'MopenEve' not implemented!")
        #event.Skip()
        global Purge

        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (2, 2))
        #Purge = cv2.morphologyEx(Purge, cv2.MORPH_OPEN, kernel, iterations=5)
        Purge = cv2.erode(Purge, kernel)

        # 清除axes中的绘图痕迹
        self.matplotlib_axes.cla()
        # 重绘
        self.matplotlib_axes.imshow(Purge, cmap=self.parent.cmap)
        self.matplotlib_axes.set_xticks([])
        self.matplotlib_axes.set_yticks([])
        self.Figure.draw()

    def dilateEve(self, event):  # wxGlade: GRPurge.<event_handler>
        #print("Event handler 'McloseEve' not implemented!")
        #event.Skip()

        global Purge

        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (2, 2))
        #Purge = cv2.morphologyEx(Purge, cv2.MORPH_CLOSE, kernel, iterations=5)
        Purge = cv2.dilate(Purge, kernel)

        # 清除axes中的绘图痕迹
        self.matplotlib_axes.cla()
        # 重绘
        self.matplotlib_axes.imshow(Purge, cmap=self.parent.cmap)
        self.matplotlib_axes.set_xticks([])
        self.matplotlib_axes.set_yticks([])
        self.Figure.draw()

    def resetEve(self, event):  # wxGlade: GRPurge.<event_handler>
        #print("Event handler 'resetEve' not implemented!")
        #event.Skip()

        global Purge

        Purge = np.copy(self.parent.Data)

        # 清除axes中的绘图痕迹
        self.matplotlib_axes.cla()
        # 重绘
        self.matplotlib_axes.imshow(Purge, cmap=self.parent.cmap)
        self.matplotlib_axes.set_xticks([])
        self.matplotlib_axes.set_yticks([])
        self.Figure.draw()

    def confirmEve(self, event):  # wxGlade: GRPurge.<event_handler>
        #print("Event handler 'confirmEve' not implemented!")
        #event.Skip()

        global Purge

        try:
            self.parent.textCtrl.SetValue(str(np.sum(Purge)))
        except:
            pass

        if self.parent.Name == 'GRfgE':
           GS.foreP = np.copy(Purge)
        if self.parent.Name == 'EE':
           GS.EE = np.copy(Purge)
        if self.parent.Name == 'VV':
           GS.VV = np.copy(Purge)
        if self.parent.Name == 'SS':
           GS.SS = np.copy(Purge)
        if self.parent.Name == 'PP':
           GS.PP = np.copy(Purge)

        # 清除axes中的绘图痕迹
        self.parent.Axes.cla()
        # 重绘
        self.parent.Axes.imshow(Purge, cmap=self.parent.cmap)
        self.parent.Axes.set_xticks([])
        self.parent.Axes.set_yticks([])
        self.parent.Figure.draw()

        self.Destroy()
        self.parent.Show()

# end of class GRPurge

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