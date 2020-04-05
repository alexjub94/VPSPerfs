import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from HttpClient import *


class GUIInterface:
    def __init__(self):
        self.fig = None
        self.a = None

        self.HttpClientRam = HttpClient("ram")
        self.HttpClientCpu = HttpClient("cpu")

        ramResponse = self.HttpClientRam.callURI()
        cpuResponse = self.HttpClientCpu.callURI()
        ramUsage = self.HttpClientRam.readContent(ramResponse)
        cpuUsage = self.HttpClientCpu.readContent(cpuResponse)

        self.ramFig = plt.Figure(figsize=(3, 3))
        self.ramFig.set_facecolor("#000000")
        self.ramA = self.ramFig.add_subplot(111)
        self.ramA.pie([100-float(ramUsage), float(ramUsage)], startangle=90, labels=[100-float(ramUsage), float(ramUsage)], autopct='%1.1f%%')
        self.ramA.legend(["free", "ram"])

        self.cpuFig = plt.Figure(figsize=(3, 3))
        self.cpuFig.set_facecolor("#000000")
        self.cpuA = self.cpuFig.add_subplot(111)
        self.cpuA.pie([100 - float(cpuUsage), float(cpuUsage)], startangle=90, labels=[100 - float(cpuUsage), float(cpuUsage)], autopct='%1.1f%%')
        self.cpuA.legend(["free", "cpu"])

        self.window = tk.Tk()
        self.window.title('VPS perfs')

        self.ramCanvas = FigureCanvasTkAgg(self.ramFig, master=self.window)
        self.ramCanvas.get_tk_widget().grid(row=0, column=0)
        self.ramCanvas.draw()

        self.cpuCanvas = FigureCanvasTkAgg(self.cpuFig, master=self.window)
        self.cpuCanvas.get_tk_widget().grid(row=0, column=1)
        self.cpuCanvas.draw()

        self.window.after(300000, self.updateInterface)
        self.window.mainloop()

    def updateInterface(self):
        print("updating")

        ramResponse = self.HttpClientRam.callURI()
        cpuResponse = self.HttpClientCpu.callURI()
        ramUsage = self.HttpClientRam.readContent(ramResponse)
        cpuUsage = self.HttpClientCpu.readContent(cpuResponse)

        self.ramA.clear()
        self.ramA.pie([100 - float(ramUsage), float(ramUsage)], startangle=90, labels=[100-float(ramUsage), float(ramUsage)], autopct='%1.1f%%')
        self.ramA.legend(["free", "ram"])
        self.ramCanvas.draw_idle()

        self.cpuA.clear()
        self.cpuA.pie([100 - float(cpuUsage), float(cpuUsage)], startangle=90, labels=[100 - float(cpuUsage), float(cpuUsage)], autopct='%1.1f%%')
        self.cpuA.legend(["free", "cpu"])
        self.cpuCanvas.draw_idle()

        self.window.after(300000, self.updateInterface)
