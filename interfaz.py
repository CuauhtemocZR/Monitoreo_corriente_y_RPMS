import sys,os
from collections import deque
import numpy as np
from PyQt4 import QtCore, QtGui,  Qt
from inicio import Ui_MainWindow
from Puerto import Ui_Dialog
from integrantes import Ui_Dialog2
import PyQt4.Qwt5 as Qwt
from PyQt4.Qwt5 import *
import serial

class Inicio(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui=Ui_MainWindow()
        self.setWindowTitle('Interfaces Electronicas')
        self.setWindowIcon(QtGui.QIcon('./Meca.png'))
        self.ui.setupUi(self)
        self.ui.Pcom.clicked.connect(self.Puerto)
        self.ui.Integra.clicked.connect(self.Info)
        self.ui.Arrancar.clicked.connect(self.enviard)
        self.ui.Detener.clicked.connect(self.enviard2)
        self.ui.Salir.clicked.connect(self.quit)
        moff=QtGui.QPixmap(".\moff.png")
        self.ui.motor.setPixmap(moff)
        self.ui.lcdRPM.setNumDigits(6)
        plot = self.ui.qwtPlot
        plot.setCanvasBackground(QtGui.QColor("black"))
        plot.setAxisTitle(Qwt.QwtPlot.yLeft, 'Corriente')
        plot.setAxisScale(Qwt.QwtPlot.yLeft, 0, 2,0.1)
        plot.setAxisAutoScale(Qwt.QwtPlot.xBottom)
        plot2 = self.ui.qwtPlot_2
        plot2.setCanvasBackground(QtGui.QColor("black"))
        plot2.setAxisTitle(Qwt.QwtPlot.yLeft, 'RPMS')
        plot2.setAxisScale(Qwt.QwtPlot.yLeft, 0, 9000,500)
        plot2.setAxisAutoScale(Qwt.QwtPlot.xBottom)
    def enviard(self):
        ser.write('A')
        moff=QtGui.QPixmap(".\mon.png")
        self.ui.motor.setPixmap(moff)
        self.tiempo_maximo = 300
        self.time = 0
        self.grafico()
        self.grafico2()
        self.startTimer(60)
    def enviard2(self):
        ser.write('B')
        moff=QtGui.QPixmap(".\moff.png")
        self.ui.motor.setPixmap(moff)
    def datos(self):
        line = ser.readline()
        line = line.strip()
        dato= line.split("|")
        Co=dato[0]
        RPS=dato[1]
        Volt=dato[2]
        Watt=dato[3]
        self.Corriente=float(Co)
        self.RPMS=int(RPS)
        self.volt=float(Volt)
        self.watt=float(Watt)
        plot = self.ui.qwtPlot
        self.ui.lcdRPM.display(self.RPMS)
        self.ui.lcdCorr.display(self.Corriente)
        self.ui.lcdVolt.display(self.volt)
        self.ui.lcdWatt.display(self.watt)
##****************************************
    def grafico(self):
        plot = self.ui.qwtPlot
        plot.setCanvasBackground(QtGui.QColor("black"))
        self.grafica = QwtPlotCurve("Canal 1") # Asignando nombre a la curva creada(grafica)
        pen = QtGui.QPen(QtGui.QColor('yellow'))
        pen.setWidth(4)
        self.grafica.setPen(pen)
        self.equis = range(0,self.tiempo_maximo,1)
        self.valores = []
        self.promedio = 0
        self.promedioMints = 0.0
        self.promedios = []
        self.minutos = 0
        self.grafica.attach(self.ui.qwtPlot)# se enlaza la curva al plano 
        
    def grafico2(self):
        plot = self.ui.qwtPlot_2
        plot.setCanvasBackground(QtGui.QColor("black"))
        self.grafica2 = QwtPlotCurve("Canal 2") # Asignando nombre a la curva creada(grafica)
        pen = QtGui.QPen(QtGui.QColor('blue'))
        pen.setWidth(4)
        self.grafica2.setPen(pen)
        self.equis2 = range(0,self.tiempo_maximo,1)
        self.valores2 = []
        self.promedio2 = 0
        self.promedioMints2 = 0.0
        self.promedios2 = []
        self.minutos2 = 0
        self.grafica2.attach(self.ui.qwtPlot_2)# se enlaza la curva al plano 
    def timerEvent(self, tiempo):
        if self.datos():
            self.time+= 1
        if self.tiempo_maximo > self.time : # Si los datos no superan los 60 datos.
            self.valores.append(self.Corriente)
            self.valores2.append(self.RPMS)
        else : #si se superan los 60 datos se elimina el dato del indice 0 y se agrega el nuevo dato.
            self.valores = self.valores[1:]
            self.valores.append(self.Corriente)
            self.valores2 = self.valores2[1:]
            self.valores2.append(self.RPMS)
            # CALCULO PROMEDIO ultimos 60 datos
            self.promedio = reduce(lambda x,y: y+x,self.valores)
            self.promedio = self.promedio/60
            self.promedio2 = reduce(lambda x,y: y+x,self.valores2)
            self.promedio2 = self.promedio2/60
            if self.time % 60 == 0 :
                self.promedios.append(self.promedio)
                self.minutos += 1
                self.promedios2.append(self.promedio2)
                self.minutos2 += 1
                if self.minutos == 2 : # 2 cambiar por average
                    self.minutos = 0
                    self.promedioMints = reduce(lambda x,y: y+x, self.promedios)
                    self.promedioMints = self.promedioMints*1.0/len(self.promedios)
                    self.promedios = []
                if self.minutos2 == 2 : # 2 cambiar por average
                    self.minutos2 = 0
                    self.promedioMints2 = reduce(lambda x,y: y+x, self.promedios2)
                    self.promedioMints2 = self.promedioMints2*1.0/len(self.promedios2)
                    self.promedios2 = []
        self.grafica.setData(self.equis,self.valores)
        self.ui.qwtPlot.replot()
        self.grafica2.setData(self.equis2,self.valores2)
        self.ui.qwtPlot_2.replot() # redibujar
##***********************************************************************        
    def quit(self):
        sys.exit(app.exec_())
    def Puerto(self):
        self.mpp = VPuerto()
        self.mpp.show()
    def Info(self):
        self.mp = VInfor()
        self.mp.show()
class VInfor(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.inte = Ui_Dialog2()
        self.inte.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./Meca.png'))
        integrantes=QtGui.QPixmap(".\MecaInfo.png")
        self.inte.inte.setPixmap(integrantes)
class VPuerto(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.Pu = Ui_Dialog()
        self.Pu.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./Meca.png'))
        self.Pu.Guardar.clicked.connect(self.guardar)
        self.Pu.Guardar.clicked.connect(self.close)
    def guardar(self):
        global ser
        x=self.Pu.PC.text()
        print x
        czr=int(x)-1
        ser = serial.Serial(czr, 115200,timeout=2)
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Inicio()
    myapp.show()
    sys.exit(app.exec_())
