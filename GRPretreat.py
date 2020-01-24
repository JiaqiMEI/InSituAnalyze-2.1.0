#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.2 on Thu Apr 11 16:09:41 2019
#

import wx
from scipy.io import loadmat
import numpy as np

import G
import Baseline2
import Derivative
import Smoothing
import SpEnd

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Pretreat.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((1300, 500))
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.Panel1 = wx.Panel(self.panel_1, wx.ID_ANY)
        figure1 = self.matplotlib_figure = Figure()
        self.matplotlib_axes1 = figure1.add_subplot(111)  # 1x1 grid, first subplot
        self.Figure1 = FigureCanvas(self.Panel1, wx.ID_ANY, figure1)
        self.RefImportBtn = wx.Button(self.Panel1, wx.ID_ANY, "Import Ref. Spectrum")
        self.AllList = wx.ListBox(self.panel_1, wx.ID_ANY, choices=["Baseline", "MSC", "SNV", "AutoScale", "MeanCenter", "S-G Smoothing", "S-G Derivative", "Normalize(area=1)", "Normalize(length=1)", "Normalize(min-max)", "None"])
        self.AddBtn = wx.Button(self.panel_1, wx.ID_ANY, u" | \n |\n▽")
        self.DelBtn = wx.Button(self.panel_1, wx.ID_ANY, u"△\n |\n |")
        self.ChoosedList = wx.ListBox(self.panel_1, wx.ID_ANY, choices=[])
        self.CalBtn = wx.Button(self.panel_1, wx.ID_ANY, "Calculate")
        self.Panel2 = wx.Panel(self.panel_1, wx.ID_ANY)
        figure2 = self.matplotlib_figure = Figure()
        self.matplotlib_axes2 = figure2.add_subplot(111)  # 1x1 grid, first subplot
        self.Figure2 = FigureCanvas(self.Panel2, wx.ID_ANY, figure2)
        self.ConfirmBtn = wx.Button(self.Panel2, wx.ID_ANY, "Confirm")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.RefImportEve, self.RefImportBtn)
        self.Bind(wx.EVT_LISTBOX, self.EvtAllList, self.AllList)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.EvtAllListDClick, self.AllList)
        self.Bind(wx.EVT_BUTTON, self.AddEve, self.AddBtn)
        self.Bind(wx.EVT_BUTTON, self.DelEve, self.DelBtn)
        self.Bind(wx.EVT_LISTBOX, self.EvtChoosedList, self.ChoosedList)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.EvtChoosedListDClick, self.ChoosedList)
        self.Bind(wx.EVT_BUTTON, self.CalculateEve, self.CalBtn)
        self.Bind(wx.EVT_BUTTON, self.ConfirmEve, self.ConfirmBtn)
        # end wxGlade

    def setParent(self, parent):
        print(parent)
        self.parent = parent

    def __set_properties(self):
        # begin wxGlade: Pretreat.__set_properties
        self.SetTitle("Pretreatment")
        self.Figure1.SetMinSize((500, 300))
        self.RefImportBtn.SetMinSize((200, 40))
        self.Panel1.SetMinSize((500, 450))
        self.AllList.SetMinSize((250, 150))
        self.AddBtn.SetMinSize((30, 60))
        self.DelBtn.SetMinSize((30, 60))
        self.ChoosedList.SetMinSize((250, 150))
        self.Figure2.SetMinSize((500, 300))
        self.ConfirmBtn.SetMinSize((200, 40))
        self.Panel2.SetMinSize((500, 450))
        self.panel_1.SetMinSize((1300, 600))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Pretreat.__do_layout
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_8.Add(self.Figure1, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_8.Add(self.RefImportBtn, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        self.Panel1.SetSizer(sizer_8)
        sizer_5.Add(self.Panel1, 1, wx.EXPAND, 0)
        sizer_5.Add((20, 20), 0, 0, 0)
        sizer_6.Add((20, 30), 0, 0, 0)
        sizer_6.Add(self.AllList, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_7.Add((20, 20), 1, 0, 0)
        sizer_7.Add(self.AddBtn, 0, wx.ALL, 5)
        sizer_7.Add(self.DelBtn, 0, wx.ALL, 5)
        sizer_7.Add((20, 20), 1, 0, 0)
        sizer_6.Add(sizer_7, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_6.Add(self.ChoosedList, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_6.Add((20, 20), 0, 0, 0)
        sizer_6.Add(self.CalBtn, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        sizer_6.Add((20, 70), 0, 0, 0)
        sizer_5.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_5.Add((20, 20), 0, 0, 0)
        sizer_9.Add(self.Figure2, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 0)
        sizer_9.Add(self.ConfirmBtn, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        self.Panel2.SetSizer(sizer_9)
        sizer_5.Add(self.Panel2, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_5)
        sizer_4.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_4)
        self.Layout()
        # end wxGlade

    def RefImportEve(self, event):  # wxGlade: Pretreat.<event_handler>
        print("Event handler 'RefImportEve' not implemented!")
        event.Skip()

        wildcard = "MAT files (*.mat)|*.mat|" \
                   "All files (*.*)|*.*"
        # "FSM files (*.fsm)|*.fsm|" \

        # 读取refData
        dlg = wx.FileDialog(self, message="Import refData",
                            defaultDir='', defaultFile='',
                            wildcard=wildcard, style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            file = dlg.GetPath()
            dlg.Destroy()

        ref = loadmat(file)

        del file

        # 参考光谱处理
        G.ref = ref[list(ref.keys())[3]]    # 自动读取
        del ref
        print(G.ref.shape)

        # 平移至ymin=0
        G.ref = G.ref - np.tile(G.ref.min(1).reshape(-1, 1), (1, G.ref.shape[1]))

        self.matplotlib_axes1.cla()
        # 绘制预处理前光谱
        self.matplotlib_axes1.plot(G.ref.T)
        self.matplotlib_axes1.set_xlabel('Wavenumber/cm-1')
        self.matplotlib_axes1.set_ylabel('Absorbance/A')
        self.matplotlib_axes1.set_xticks([])
        self.Figure1.draw()


        dlg1 = wx.MessageDialog(None, 'Whether the characteristic band has been intercepted?',
                                'MessageDialog', wx.YES_NO | wx.ICON_QUESTION)

        if dlg1.ShowModal() == wx.ID_YES:
            dlg1.Destroy()
            G.refN = np.copy(G.ref)
            k, G.HyperDataN, G.WaveN = self.SpCut([], G.HyperData, G.WaveNumber)
            print(k)
            del k

        else:
            dlg1.Destroy()
            dlg2 = wx.MessageDialog(None, 'Intercepting characteristic band NOW?',
                                    'MessageDialog', wx.YES_NO | wx.ICON_QUESTION)

            if dlg2.ShowModal() == wx.ID_YES:
                dlg2.Destroy()
                G.refN, G.HyperDataN, G.WaveN = self.SpCut(G.ref, G.HyperData, G.WaveNumber)

            else:
                G.refN = np.copy(G.ref)
                G.HyperDataN = np.copy(G.HyperData)
                G.WaveN = np.copy(G.WaveNumber)

        print(G.refN.shape)
        print(G.HyperDataN.shape)
        # 清除axes中的绘图痕迹
        self.matplotlib_axes1.cla()
        # 绘制预处理前光谱
        self.matplotlib_axes1.plot(G.refN.T)
        self.matplotlib_axes1.set_xlabel('Wavenumber/cm-1')
        self.matplotlib_axes1.set_ylabel('Absorbance/A')
        self.matplotlib_axes1.set_xticks([])
        # self.matplotlib_axes1.set_yticks([])
        self.Figure1.draw()

    def SpCut(self, Sp1, Sp2, Wavenumber):
        dlg = SpEnd.MyDialog(self)
        dlg.ShowModal()

        print(G.spEndL, G.spEndR)
        indexL = np.argwhere(Wavenumber == G.spEndL)
        print(indexL[0][1])
        indexR = np.argwhere(Wavenumber == G.spEndR)
        print(indexR)

        try:
            Sp1N = Sp1[:, int(indexL[0][1]):int(indexR[0][1]+1)]
        except Exception as err:
            Sp1N = []
        try:
            Sp2N = Sp2[:, int(indexL[0][1]):int(indexR[0][1]+1)]
        except Exception as err:
            Sp2N = []

        WaveN = Wavenumber[:, int(indexL[0][1]):int(indexR[0][1]+1)]

        return Sp1N, Sp2N, WaveN

    def CalculateEve(self, event):  # wxGlade: Pretreat.<event_handler>
        #print("Event handler 'CalculateEve' not implemented!")
        #event.Skip()

        # 计算预处理后光谱

        ref = np.copy(G.refN)
        HyperData = np.copy(G.HyperDataN)

        # 一旦重新计算，则先删除预处理算法记录
        del G.SpList
        # 获取新的预处理算法记录，作为“全局变量”保存，保存到最终文件中
        G.SpList = self.ChoosedList.GetItems()

        for x in G.SpList:
            if x == 'Baseline':
                #ref = G.Masymcorr(ref, G.BaselineLambda, G.BaselineP)
                #HyperData = G.Masymcorr(HyperData, G.BaselineLambda, G.BaselineP)
                #30+小时

                #ref = G.baseline_als(ref, G.BaselineLambda, G.BaselineP)
                #HyperData = G.baseline_als(HyperData, G.BaselineLambda, G.BaselineP)

                ref = G.airPLS(ref, lambda_=G.BaselineLambda, porder=G.BaselineOrder, itermax=G.BaselineIter)
                HyperData = G.airPLS(HyperData, lambda_=G.BaselineLambda, porder=G.BaselineOrder, itermax=G.BaselineIter)
                #airPLS(X, lambda_=100, porder=1, itermax=15)
                #2分钟

                #ref = G.baseline_correction(ref, block_size=101, polyorder=3, show_graph=False)
                #HyperData = G.baseline_correction(HyperData, block_size=101, polyorder=3, show_graph=False)
                #baseline_correction(X, block_size=101, polyorder=3, show_graph=False)
                #80分钟

            elif x == 'MSC':
                refmean = np.mean(ref, 0)
                ref = G.Mmsc(ref, refmean)

                HyperDatamean = np.mean(HyperData, 0)
                HyperData = G.Mmsc(HyperData, refmean)

            elif x == 'SNV':
                ref = G.Msnv(ref)
                HyperData = G.Msnv(HyperData)

            elif x == 'AutoScale':
                ref = G.Mautoscale(ref)
                HyperData = G.Mautoscale(HyperData)

            elif x == 'MeanCenter':
                ref = G.Mmeancenter(ref)
                HyperData = G.Mmeancenter(HyperData)

            elif x == 'S-G Smoothing':
                ref = G.MsgSD(ref, G.SWidth, G.SOrder, 0)
                HyperData = G.MsgSD(HyperData, G.SWidth, G.SOrder, 0)

            elif x == 'S-G Derivative':
                ref = G.MsgSD(ref, G.DWidth, G.DOrder, G.Deriv)
                HyperData = G.MsgSD(HyperData, G.DWidth, G.DOrder, G.Deriv)

            # normtype = the type of norm to use {default = 2}. The following are
            # typical values of normtype:
            # normtype        description               norm
            # 1         normalize to unit area       sum(abs(dat))
            # 2         normalize to unit LENGTH     sqrt(sum(dat^2))
            # 3(inf)    normalize to maximum value   max(dat)
            # Generically,
            # for row i of dat:
            # norms(i) = sum(abs(dat(i,:)).^normtype)^(1/normtype)
            # If (normtype) is specified then (out) must be included, although it can be empty []

            elif x == 'Normalize(area=1)':
                ref = G.Mnormalize(ref, 1)
                HyperData = G.Mnormalize(HyperData, 1)

            elif x == 'Normalize(length=1)':
                ref = G.Mnormalize(ref, 2)
                HyperData = G.Mnormalize(HyperData, 2)

            elif x == 'Normalize(min-max)':
                ref = G.Mnormalize(ref, 3)
                HyperData = G.Mnormalize(HyperData, 3)

            elif x == 'None':
                pass
            else:
                pass

        G.refp = np.copy(ref)
        G.HyperDatap = np.copy(HyperData)
        G.HyperDatapAve = np.mean(HyperData, 1).reshape(G.m, G.n)

        # 清除axes中的绘图痕迹
        self.matplotlib_axes2.cla()
        # 绘制预处理后光谱
        self.matplotlib_axes2.plot(G.refp.T)
        self.matplotlib_axes2.set_xlabel('Wavenumber/cm-1')
        self.matplotlib_axes2.set_ylabel('Absorbance/A')
        self.matplotlib_axes2.set_xticks([])
        #self.matplotlib_axes2.set_yticks([])
        self.Figure2.draw()

    def ConfirmEve(self, event):  # wxGlade: Pretreat.<event_handler>
        #print("Event handler 'ComfirmEve' not implemented!")
        #event.Skip()

        self.Destroy()
        self.parent.Show()

    # 单击事件
    def EvtAllList(self, event):  # wxGlade: Pretreat.<event_handler>
        #print("Event handler 'EvtAllList' not implemented!")
        #event.Skip()

        global K
        global KK
        K = event.GetString()
        KK = event.GetSelection()
        #print(K)

    def AddEve(self, event):  # wxGlade: Pretreat.<event_handler>
        #print("Event handler 'AddEve' not implemented!")
        #event.Skip()

        global K
        global KK

        self.setPara(KK)
        self.ChoosedList.Append(K)      ###Append

    # 双击事件
    def EvtAllListDClick(self, event):  # wxGlade: Pretreat.<event_handler>
        print("Event handler 'EvtAllListDClick' not implemented!")
        event.Skip()

        K = event.GetString()
        KK = event.GetSelection()
        self.setPara(KK)
        self.ChoosedList.Append(K)

    def setPara(self, index):
        if index == 0:
            pass
            self.frame = Baseline2.MyFrame(None, wx.ID_ANY, "")
            self.frame.Show()

        elif index == 5:
            self.frame = Smoothing.MyFrame(None, wx.ID_ANY, "")
            self.frame.Show()

        elif index == 6:
            self.frame = Derivative.MyFrame(None, wx.ID_ANY, "")
            self.frame.Show()

    def EvtChoosedList(self, event):  # wxGlade: Pretreat.<event_handler>
        print("Event handler 'EvtChoosedList' not implemented!")
        event.Skip()

        global KK
        KK = event.GetSelection()
        print(KK)

    def DelEve(self, event):  # wxGlade: Pretreat.<event_handler>
        print("Event handler 'DelEve' not implemented!")
        event.Skip()

        global KK
        self.ChoosedList.Delete(KK)      ###Delete

    def EvtChoosedListDClick(self, event):  # wxGlade: Pretreat.<event_handler>
        print("Event handler 'EvtChoosedListDClick' not implemented!")
        event.Skip()

        global KK
        KK = event.GetSelection()
        self.ChoosedList.Delete(KK)

# end of class Pretreat

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
