# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 00:16:31 2020

@author: Javier Ojeda Prieto
"""
import sys
import math
import os
import subprocess
import numpy as np
from interfazCalculosStyle import *
from lectura2 import *
import pyqtgraph as pg
from popUpWarning import Ui_popUp
from info import Ui_Info
from freqWindow import Ui_Freq
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QIcon, QSystemTrayIcon, QMenu
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QFileInfo

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,parent, *args, **kwargs):
        super(MainWindow, self).__init__(parent)
        ultimo=9998
        # ensure this window gets garbage-collected when closed
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        QtWidgets.QMainWindow.__init__(self, parent, *args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QIcon('iconn.png'))      
            
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint) #Elimina las flags (boton cerrar, minimizar, maximizar superior)
        self.comboBox_2.activated.connect(self.comprobarFrecuencias)
        self.comboBox_3.activated.connect(self.comprobarTerrenos)
        self.comboBox_4.activated.connect(self.actualizaTerreno1)
        self.comboBox_5.activated.connect(self.actualizaTerreno2)
        self.comboBox_6.activated.connect(self.actualizaTerreno3)
        self.comboBox_7.activated.connect(self.actualizaTerreno4)
        self.comboBox.activated.connect(self.actualizaTerreno)
        self.button_iniciar.clicked.connect(self.secuencia)
        self.button_iniciar_2.clicked.connect(self.secuenciaMixta)
        self.button_limpiar.clicked.connect(self.clearr)
        self.button_limpiar_2.clicked.connect(self.clearr_2)
        self.pushButton_2.clicked.connect(self.calculaDistancia)
        self.button_cerrar.clicked.connect(self.regresar)
        self.button_cerrar_2.clicked.connect(self.regresar)
        self.button_exportar.clicked.connect(self.saveFig1)        
        self.button_exportar_2.clicked.connect(self.saveFig2)
        self.pushButton_7.clicked.connect(self.informacion)
        self.pushButton.clicked.connect(self.informacion)
        self.pushButton_3.clicked.connect(self.infoFreq)
        
        
    ##################################################################################
    # FUNCIONES TERRENO HOMOGENEO
        
    def infoFreq(self): #Abre informacion sobre uso de multiples frecuencias
        self.ventanaFreq=QtWidgets.QMainWindow()
        self.ui=Ui_Freq()
        self.ui.setupUi(self.ventanaFreq)
        self.ventanaFreq.setWindowFlags(QtCore.Qt.WindowCloseButtonHint);
        self.ventanaFreq.setWindowIcon(QIcon("iconn.png"))
        self.ventanaFreq.show()
                       
    def regresar(self): #Funcion usada en ambas pestañas
        self.close() #cierra ventana actual de calculos
        self.parent().show() #vuelve a mostrar ventana de bienvenida, padre de la actual   
    
    def inhabilitaSigEps(self): #cuando se ha seleccionado un terreno predeterminado, las casillas de sigma y epsilon se configuran para solo lectura
        self.SIGMA.setReadOnly(True)
        self.EPSLON.setReadOnly(True)
        self.SIGMA.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.EPSLON.setStyleSheet("background-color: rgb(235, 235, 235);")

    def actualizaTerreno(self): #En funcion del valor seleccionado del desplegable de terrenos, actualiza casillas de sigma y epsilon
        terreno = self.comboBox.currentText()
        if(terreno=="Agua del mar, salinidad baja"):
            self.SIGMA.setText("1")
            self.EPSLON.setText("80")
            self.inhabilitaSigEps() #como es un terreno predeterminado, se ponen casillas de sigma y epsilon en modo solo lectura           
        elif(terreno=="Agua del mar, salinidad media"):
            self.SIGMA.setText("5")
            self.EPSLON.setText("70")
            self.inhabilitaSigEps()
        elif(terreno=="Agua dulce"):
            self.SIGMA.setText("0.003")
            self.EPSLON.setText("80")
            self.inhabilitaSigEps()
        elif(terreno=="Tierra"):
            self.SIGMA.setText("0.03")
            self.EPSLON.setText("40")
            self.inhabilitaSigEps()
        elif(terreno=="Tierra húmeda"):
            self.SIGMA.setText("0.01")
            self.EPSLON.setText("30")
            self.inhabilitaSigEps()
        elif(terreno=="Tierra moderadamente seca"):
            self.SIGMA.setText("0.001")
            self.EPSLON.setText("15")
            self.inhabilitaSigEps()
        elif(terreno=="Tierra seca"):
            self.SIGMA.setText("0.0003")
            self.EPSLON.setText("7")
            self.inhabilitaSigEps()
        elif(terreno=="Tierra muy seca"):
            self.SIGMA.setText("0.0001")
            self.EPSLON.setText("3")
            self.inhabilitaSigEps()
        elif(terreno=="Hielo de agua dulce, -1ºC"):
            self.SIGMA.setText("0.00003")
            self.EPSLON.setText("3")
            self.inhabilitaSigEps()
        elif(terreno=="Hielo de agua dulce, -10ºC"):
            self.SIGMA.setText("-0.00001")
            self.EPSLON.setText("3")
            self.inhabilitaSigEps()
        elif(terreno=="Personalizado"):
            self.SIGMA.setText("")
            self.EPSLON.setText("")
            self.SIGMA.setReadOnly(False) #se desactiva modo solo lectura para sigma y epsilon
            self.EPSLON.setReadOnly(False)
            self.SIGMA.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.EPSLON.setStyleSheet("background-color: rgb(255, 255, 255);")
            
    def comprobarFrecuencias(self): #comprueba que numero de frecuencias se ha seleccionado en el desplegable, y oculta o muestra las casillas necesarias para ello
        comboText = self.comboBox_2.currentText()
        if (comboText=="1"):
            self.FREQ_2.setVisible(False) #oculta casilla de frecuencia 2
            self.label_11.setVisible(False) #oculta etiqueta de frecuencia 2
            self.label_12.setVisible(False) #oculta etiqueta de MHz de la frecuencia 2
            self.FREQ_3.setVisible(False) #igual, para frecuencia 3
            self.label_15.setVisible(False)
            self.label_17.setVisible(False)
            self.FREQ_4.setVisible(False)
            self.label_16.setVisible(False)
            self.label_18.setVisible(False)
            self.FREQ_5.setVisible(False)
            self.label_19.setVisible(False)
            self.label_21.setVisible(False)
            self.FREQ_6.setVisible(False)
            self.label_20.setVisible(False)
            self.label_23.setVisible(False)
            self.FREQ_7.setVisible(False)
            self.label_25.setVisible(False)
            self.label_26.setVisible(False)
            self.FREQ_8.setVisible(False)
            self.label_24.setVisible(False)
            self.label_22.setVisible(False)            
            self.lineEdit.setReadOnly(False) #como es solo una frecuencia, activa lo necesario para calcular la distancia
            self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")            
        elif (comboText=="2"):
            self.FREQ_2.setVisible(True)
            self.label_11.setVisible(True)
            self.label_12.setVisible(True)
            self.FREQ_3.setVisible(False)
            self.label_15.setVisible(False)
            self.label_17.setVisible(False)
            self.FREQ_4.setVisible(False)
            self.label_16.setVisible(False)
            self.label_18.setVisible(False)
            self.FREQ_5.setVisible(False)
            self.label_19.setVisible(False)
            self.label_21.setVisible(False)
            self.FREQ_6.setVisible(False)
            self.label_20.setVisible(False)
            self.label_23.setVisible(False)
            self.FREQ_7.setVisible(False)
            self.label_25.setVisible(False)
            self.label_26.setVisible(False)
            self.FREQ_8.setVisible(False)
            self.label_24.setVisible(False)
            self.label_22.setVisible(False)
            self.ocultaDistancia() #oculta el calculo de distancia porque a mas de una frecuencia no esta disponible            
        elif (comboText=="3"):
            self.FREQ_2.setVisible(True)
            self.label_11.setVisible(True)
            self.label_12.setVisible(True)
            self.FREQ_3.setVisible(True)
            self.label_15.setVisible(True)
            self.label_17.setVisible(True)
            self.FREQ_4.setVisible(False)
            self.label_16.setVisible(False)
            self.label_18.setVisible(False)
            self.FREQ_5.setVisible(False)
            self.label_19.setVisible(False)
            self.label_21.setVisible(False)
            self.FREQ_6.setVisible(False)
            self.label_20.setVisible(False)
            self.label_23.setVisible(False)
            self.FREQ_7.setVisible(False)
            self.label_25.setVisible(False)
            self.label_26.setVisible(False)
            self.FREQ_8.setVisible(False)
            self.label_24.setVisible(False)
            self.label_22.setVisible(False)
            self.ocultaDistancia()            
        elif (comboText=="4"):
            self.FREQ_2.setVisible(True)
            self.label_11.setVisible(True)
            self.label_12.setVisible(True)
            self.FREQ_3.setVisible(True)
            self.label_15.setVisible(True)
            self.label_17.setVisible(True)
            self.FREQ_4.setVisible(True)
            self.label_16.setVisible(True)
            self.label_18.setVisible(True)
            self.FREQ_5.setVisible(False)
            self.label_19.setVisible(False)
            self.label_21.setVisible(False)
            self.FREQ_6.setVisible(False)
            self.label_20.setVisible(False)
            self.label_23.setVisible(False)
            self.FREQ_7.setVisible(False)
            self.label_25.setVisible(False)
            self.label_26.setVisible(False)
            self.FREQ_8.setVisible(False)
            self.label_24.setVisible(False)
            self.label_22.setVisible(False)
            self.ocultaDistancia()            
        elif (comboText=="5"):
            self.FREQ_2.setVisible(True)
            self.label_11.setVisible(True)
            self.label_12.setVisible(True)
            self.FREQ_3.setVisible(True)
            self.label_15.setVisible(True)
            self.label_17.setVisible(True)
            self.FREQ_4.setVisible(True)
            self.label_16.setVisible(True)
            self.label_18.setVisible(True)
            self.FREQ_5.setVisible(True)
            self.label_19.setVisible(True)
            self.label_21.setVisible(True)
            self.FREQ_6.setVisible(False)
            self.label_20.setVisible(False)
            self.label_23.setVisible(False)
            self.FREQ_7.setVisible(False)
            self.label_25.setVisible(False)
            self.label_26.setVisible(False)
            self.FREQ_8.setVisible(False)
            self.label_24.setVisible(False)
            self.label_22.setVisible(False)
            self.ocultaDistancia()          
        elif (comboText=="6"):
            self.FREQ_2.setVisible(True)
            self.label_11.setVisible(True)
            self.label_12.setVisible(True)
            self.FREQ_3.setVisible(True)
            self.label_15.setVisible(True)
            self.label_17.setVisible(True)
            self.FREQ_4.setVisible(True)
            self.label_16.setVisible(True)
            self.label_18.setVisible(True)
            self.FREQ_5.setVisible(True)
            self.label_19.setVisible(True)
            self.label_21.setVisible(True)
            self.FREQ_6.setVisible(True)
            self.label_20.setVisible(True)
            self.label_23.setVisible(True)
            self.FREQ_7.setVisible(False)
            self.label_25.setVisible(False)
            self.label_26.setVisible(False)
            self.FREQ_8.setVisible(False)
            self.label_24.setVisible(False)
            self.label_22.setVisible(False)
            self.ocultaDistancia()          
        elif (comboText=="7"):
            self.FREQ_2.setVisible(True)
            self.label_11.setVisible(True)
            self.label_12.setVisible(True)
            self.FREQ_3.setVisible(True)
            self.label_15.setVisible(True)
            self.label_17.setVisible(True)
            self.FREQ_4.setVisible(True)
            self.label_16.setVisible(True)
            self.label_18.setVisible(True)
            self.FREQ_5.setVisible(True)
            self.label_19.setVisible(True)
            self.label_21.setVisible(True)
            self.FREQ_6.setVisible(True)
            self.label_20.setVisible(True)
            self.label_23.setVisible(True)
            self.FREQ_7.setVisible(True)
            self.label_25.setVisible(True)
            self.label_26.setVisible(True)
            self.FREQ_8.setVisible(False)
            self.label_24.setVisible(False)
            self.label_22.setVisible(False)
            self.ocultaDistancia()       
        elif (comboText=="8"):
            self.FREQ_2.setVisible(True)
            self.label_11.setVisible(True)
            self.label_12.setVisible(True)
            self.FREQ_3.setVisible(True)
            self.label_15.setVisible(True)
            self.label_17.setVisible(True)
            self.FREQ_4.setVisible(True)
            self.label_16.setVisible(True)
            self.label_18.setVisible(True)
            self.FREQ_5.setVisible(True)
            self.label_19.setVisible(True)
            self.label_21.setVisible(True)
            self.FREQ_6.setVisible(True)
            self.label_20.setVisible(True)
            self.label_23.setVisible(True)
            self.FREQ_7.setVisible(True)
            self.label_25.setVisible(True)
            self.label_26.setVisible(True)
            self.FREQ_8.setVisible(True)
            self.label_24.setVisible(True)
            self.label_22.setVisible(True)
            self.ocultaDistancia()   
      
    def comprobarWarning(self): #se comprueba que ningun parametro introducido esta vacio, a excepcion de las frecuencias 2-3-4-5-6-7-8
        if(self.HTT.text()=="" or self.HRR.text()=="" or self.SIGMA.text()=="" 
           or self.EPSLON.text()=="" or self.FREQ.text()==""):
            parar=True #si hay alguno vacio, se debe parar la ejecucion
            self.lanzarWarning("Es necesario rellenar todos los campos") #se lanza ventana emergente con error especificado
        #Se comprueba que todos los valores introducidos estan en formato float, a excepcion de frecuencias 2-3-4-5-6-7-8
        elif (self.is_float(self.HTT.text())==False or self.is_float(self.HRR.text())==False or 
              self.is_float(self.SIGMA.text())==False or self.is_float(self.EPSLON.text())==False or 
              self.is_float(self.FREQ.text())==False):
            parar=True
            self.lanzarWarning("Los parámetros deben ser formato float")
            
        elif(float(self.FREQ.text())>30 or float(self.FREQ.text())<0.01): #se comprueba que la frecuencia 1 esta dentro del rango (10 kHz-30 MHz)
            self.lanzarWarning("La frecuencia debe estar entre \n 10 KHz y 30 MHz")
            parar=True
        else: #si no hay errores, no se para la ejecucion
            parar=False
        return parar
        
    def lanzarWarning(self,texto): #Usada en ambas pestañas. Muestra ventanas emergentes para notificar errores.
        self.ventana=QtWidgets.QMainWindow() #crea un QMainWindow
        self.ui=Ui_popUp() #crea un objeto con el constructor de Ui_popUp
        self.ui.setupUi(self.ventana) #a ese objeto le aplica la configuracion setupUi, pasandole la ventana a la que se lo aplicará
        self.ui.labelError.setText(texto) #a la etiqueta de error le introduce el texto que se quiere mostrar como error
        self.ventana.setWindowFlags(QtCore.Qt.WindowCloseButtonHint); #solo el boton de cerrar esta disponible, ni minimizar ni maximizar
        self.ventana.setWindowIcon(QIcon("warning.png")) #icono de ventana, el de la aplicacion
        self.ventana.show()        #muestra la ventana

    def calculaRango(self, frecuencia): #Usada en ambas pestañas. Comprueba que el rango de frecuencia contiene a la frecuencia introducida
        if(float(frecuencia)>30 or float(frecuencia)<0.01):
            return 1
        else:
            return 0
        
    def compruebaAltura(self,HRR,SIGMA,EPSLON,FREQ): #Usada en ambas pestañas
        #Comprueba que la altura de antena receptora cumpla dos condiciones. Vease pagina 3 de Rec. P.368-9 de la ITU-R
        c=300
        landa=c/FREQ
        cond1=60*landa*SIGMA
        cond2=1.2*math.sqrt(SIGMA)*math.sqrt(landa*landa*landa)
        if(100*EPSLON<cond1 and HRR>=cond2):
            return True
        else:
            return False
        
    def is_float(self,cadena): #Usada en ambas pestañas
        try:
            float(cadena)
            return True #si ha ido bien la conversion, es float y se devuelve True
        except ValueError:
            return False #si ha ido mal la conversion, no es float y se devuelve False              

    def secuencia(self): #en funcion de cuantas frecuencias se hayan seleccionado, se obtendran los valores de esas frecuencias y se llamara a Generar datos para grafica
    #tantas veces como numero de frecuencias se hayan seleccionado. Para que cada curva sea independiente
        self.clearr() #se limpia grafica anterior, para evitar mezclar resultados y que el usuario no tenga que limpiarla manualmente
        comboText = self.comboBox_2.currentText()
        parar=self.comprobarWarning() #comprueba que no existen errores principales de rango de frecuencia, parametros incompletos...
        if (parar==False): #si todo ha ido bien en la comprobacion anterior
            if (comboText=="1"): #si el numero de frecuencias es 1
                self.lineEdit.setReadOnly(False) #activa el calculo de distancia
                self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
                FREQ=self.FREQ.text() #selecciona valor de frecuencia
                Label1='f='+FREQ+' MHz' #prepara etiqueta para leyenda de grafica
                self.generar(FREQ,'#0093FF',Label1) #se llama a funcion que genera datos para grafica y su representacion, con etiqueta y un color para esta frecuencia
            elif (comboText=="2"): #si numero de frecuencias es 2
                if (self.FREQ_2.text()==""): #comprueba que la freq2 no esta vacia
                    self.lanzarWarning("Es necesario rellenar todos los campos")
                elif(self.is_float(self.FREQ_2.text())==False): #comprueba que es un valor entero o decimal
                    self.lanzarWarning("Los parámetros deben ser formato float")
                else:
                    if (self.calculaRango(self.FREQ_2.text())==1): #comprueba su rango
                        self.lanzarWarning("Las frecuencias deben estar entre \n 10 KHz y 30 MHz")
                    else:
                        FREQ=self.FREQ.text() #obtiene valores de frecuencias 1 y 2, con sus etiquetas y colores, y se generan sus curvas en la grafica
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#0093FF',Label1)
                        FREQ=self.FREQ_2.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ, '#FFB726',Label1)
            elif (comboText=="3"): #se repite todo el proceso recogiendo y comprobando los datos de tres frecuencias
                if (self.FREQ_2.text()=="" or self.FREQ_3.text()==""):
                    self.lanzarWarning("Es necesario rellenar todos los campos")
                elif(self.is_float(self.FREQ_2.text())==False or self.is_float(self.FREQ_3.text())==False):
                    self.lanzarWarning("Los parámetros deben ser formato float")
                else:
                    if (self.calculaRango(self.FREQ_2.text())==1 or self.calculaRango(self.FREQ_3.text())==1):
                        self.lanzarWarning("Las frecuencias deben estar entre \n 10 KHz y 30 MHz")
                    else:
                        FREQ=self.FREQ.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#0093FF',Label1)
                        FREQ=self.FREQ_2.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ, '#FFB726',Label1)
                        FREQ=self.FREQ_3.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#60C146',Label1)
            elif (comboText=="4"):
                if (self.FREQ_2.text()=="" or self.FREQ_3.text()=="" or self.FREQ_4.text()==""):
                    self.lanzarWarning("Es necesario rellenar todos los campos")
                elif(self.is_float(self.FREQ_2.text())==False or self.is_float(self.FREQ_3.text())==False
                     or self.is_float(self.FREQ_4.text())==False):
                    self.lanzarWarning("Los parámetros deben ser formato float")
                else:
                    if (self.calculaRango(self.FREQ_2.text())==1 or self.calculaRango(self.FREQ_3.text())==1 
                        or self.calculaRango(self.FREQ_4.text())==1):
                        self.lanzarWarning("Las frecuencias deben estar entre \n 10 KHz y 30 MHz")
                    else:
                        FREQ=self.FREQ.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#0093FF',Label1)
                        FREQ=self.FREQ_2.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ, '#FFB726',Label1)
                        FREQ=self.FREQ_3.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#60C146',Label1)
                        FREQ=self.FREQ_4.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#BE54C7',Label1)
            elif (comboText=="5"):
                if (self.FREQ_2.text()=="" or self.FREQ_3.text()=="" or self.FREQ_4.text()==""
                     or self.FREQ_5.text()==""):
                    self.lanzarWarning("Es necesario rellenar todos los campos")
                elif(self.is_float(self.FREQ_2.text())==False or self.is_float(self.FREQ_3.text())==False
                     or self.is_float(self.FREQ_4.text())==False or self.is_float(self.FREQ_5.text())==False):
                    self.lanzarWarning("Los parámetros deben ser formato float")
                else:
                    if (self.calculaRango(self.FREQ_2.text())==1 or self.calculaRango(self.FREQ_3.text())==1 
                        or self.calculaRango(self.FREQ_4.text())==1 or self.calculaRango(self.FREQ_5.text())==1):
                        self.lanzarWarning("Las frecuencias deben estar entre \n 10 KHz y 30 MHz")
                    else:
                        FREQ=self.FREQ.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#0093FF',Label1)
                        FREQ=self.FREQ_2.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ, '#FFB726',Label1)
                        FREQ=self.FREQ_3.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#60C146',Label1)
                        FREQ=self.FREQ_4.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#BE54C7',Label1)
                        FREQ=self.FREQ_5.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#50DCA5',Label1)
            elif (comboText=="6"):
                if (self.FREQ_2.text()=="" or self.FREQ_3.text()=="" or self.FREQ_4.text()==""
                     or self.FREQ_5.text()=="" or self.FREQ_6.text()==""):
                    self.lanzarWarning("Es necesario rellenar todos los campos")
                elif(self.is_float(self.FREQ_2.text())==False or self.is_float(self.FREQ_3.text())==False
                     or self.is_float(self.FREQ_4.text())==False or self.is_float(self.FREQ_5.text())==False
                     or self.is_float(self.FREQ_6.text())==False):
                    self.lanzarWarning("Los parámetros deben ser formato float")
                else:
                    if (self.calculaRango(self.FREQ_2.text())==1 or self.calculaRango(self.FREQ_3.text())==1 
                        or self.calculaRango(self.FREQ_4.text())==1 or self.calculaRango(self.FREQ_5.text())==1
                        or self.calculaRango(self.FREQ_6.text())==1):
                        self.lanzarWarning("Las frecuencias deben estar entre \n 10 KHz y 30 MHz")
                    else:
                        FREQ=self.FREQ.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#0093FF',Label1)
                        FREQ=self.FREQ_2.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ, '#FFB726',Label1)
                        FREQ=self.FREQ_3.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#60C146',Label1)
                        FREQ=self.FREQ_4.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#BE54C7',Label1)
                        FREQ=self.FREQ_5.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#50DCA5',Label1)
                        FREQ=self.FREQ_6.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#808080',Label1)
            elif (comboText=="7"):
                if (self.FREQ_2.text()=="" or self.FREQ_3.text()=="" or self.FREQ_4.text()==""
                     or self.FREQ_5.text()=="" or self.FREQ_6.text()=="" or self.FREQ_7.text()==""):
                    self.lanzarWarning("Es necesario rellenar todos los campos")
                else:
                    if (self.calculaRango(self.FREQ_2.text())==1 or self.calculaRango(self.FREQ_3.text())==1 
                        or self.calculaRango(self.FREQ_4.text())==1 or self.calculaRango(self.FREQ_5.text())==1
                        or self.calculaRango(self.FREQ_6.text())==1 or self.calculaRango(self.FREQ_7.text())==1):
                        self.lanzarWarning("Las frecuencias deben estar entre \n 10 KHz y 30 MHz")
                    elif(self.is_float(self.FREQ_2.text())==False or self.is_float(self.FREQ_3.text())==False
                         or self.is_float(self.FREQ_4.text())==False or self.is_float(self.FREQ_5.text())==False
                         or self.is_float(self.FREQ_6.text())==False or self.is_float(self.FREQ_7.text())==False):
                        self.lanzarWarning("Los parámetros deben ser formato float")
                    else:
                        FREQ=self.FREQ.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#0093FF',Label1)
                        FREQ=self.FREQ_2.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ, '#FFB726',Label1)
                        FREQ=self.FREQ_3.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#60C146',Label1)
                        FREQ=self.FREQ_4.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#BE54C7',Label1)
                        FREQ=self.FREQ_5.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#50DCA5',Label1)
                        FREQ=self.FREQ_6.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#808080',Label1)
                        FREQ=self.FREQ_7.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#7C1A2F',Label1)
            elif (comboText=="8"):
                if (self.FREQ_2.text()=="" or self.FREQ_3.text()=="" or self.FREQ_4.text()==""
                     or self.FREQ_5.text()=="" or self.FREQ_6.text()=="" 
                     or self.FREQ_7.text()=="" or self.FREQ_8.text()==""):
                    self.lanzarWarning("Es necesario rellenar todos los campos")
                elif(self.is_float(self.FREQ_2.text())==False or self.is_float(self.FREQ_3.text())==False
                         or self.is_float(self.FREQ_4.text())==False or self.is_float(self.FREQ_5.text())==False
                         or self.is_float(self.FREQ_6.text())==False or self.is_float(self.FREQ_7.text())==False
                         or self.is_float(self.FREQ_8.text())==False):
                        self.lanzarWarning("Los parámetros deben ser formato float")
                else:
                    if (self.calculaRango(self.FREQ_2.text())==1 or self.calculaRango(self.FREQ_3.text())==1 
                        or self.calculaRango(self.FREQ_4.text())==1 or self.calculaRango(self.FREQ_5.text())==1
                        or self.calculaRango(self.FREQ_6.text())==1 or self.calculaRango(self.FREQ_7.text())==1
                        or self.calculaRango(self.FREQ_8.text())==1):
                        self.lanzarWarning("Las frecuencias deben estar entre \n 10 KHz y 30 MHz")
                    else:
                        FREQ=self.FREQ.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#0093FF',Label1)
                        FREQ=self.FREQ_2.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ, '#FFB726',Label1)
                        FREQ=self.FREQ_3.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#60C146',Label1)
                        FREQ=self.FREQ_4.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#BE54C7',Label1)
                        FREQ=self.FREQ_5.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#50DCA5',Label1)
                        FREQ=self.FREQ_6.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#808080',Label1)
                        FREQ=self.FREQ_7.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#7C1A2F',Label1)
                        FREQ=self.FREQ_8.text()
                        Label1='f='+FREQ+' MHz'
                        self.generar(FREQ,'#FF4711',Label1)

    def generar(self,FREQ,color,label):
        global ultimo
        HTT=self.HTT.text() #recoge textos de los parametros introducidos
        HRR=self.HRR.text()
        SIGMA=self.SIGMA.text()
        EPSLON=self.EPSLON.text()
        if(self.compruebaAltura(float(HRR), float(SIGMA),float(EPSLON), float(FREQ)) == True): #comprueba que la altura receptora cumple una restriccion de la ITU-R P.368
            self.lanzarWarning("Cuando εᵣ≪60λσ, debe elegir altura \n antena receptora tal que h<√σ√λ³ \n Fallo para frecuencia:"+FREQ+" MHz")
        else:
            if self.Horizontal.isChecked():
                IPOLRN='2' #Para GRWAVE, 2 es horizontal y 1 es vertical en el parametro IPOLRN
            elif self.Vertical.isChecked():
                IPOLRN='1'
            #Se itera durante 4 veces. Cada curva será consecuencia de 4 llamadas a GRWAVE. Para que la escala logaritmica del eje X, segmentada en 4 divisiones, tenga en cada
            #una de ellas los mismos puntos (100), se ha hecho eso. Cada uno tiene un dstep distinto para asegurar que hay 100 puntos en cada division.
            for i in [0, 1, 2, 3]:
                if i==0:
                    dmin='1'
                    dmax='10'
                    dstep='0.1'
                    inicial=1; #marca si en el fichero de salida se debe empezar a escribir desde cero (por ser la primera vez), o continuando al final del fichero sin borrar lo ya escrito
                elif i==1:
                    dmin='10'
                    dmax='100'
                    dstep='1'
                    inicial=0;
                elif i==2:
                    dmin='100'
                    dmax='1000'
                    dstep='10'
                    inicial=0;
                elif i==3:
                    dmin='1000'
                    dmax='10000'
                    dstep='100'
                    inicial=0;
                self.rellenarEntrada(HTT,HRR,FREQ,SIGMA,EPSLON,IPOLRN,dmin,dmax,dstep) #se rellena fichero de entrada para GRWAVE, entrada.dat
                seguir=self.empezar(inicial) #realiza llamada a grwave y recoge datos de salida. Variable SEGUIR indica si ha habido fallo en la seleccion del entorno Windows o MSDOS.
            if(seguir==True): #no ha habido fallo ejecutando GRWAVE 
                d_km, intensidad,perdidas=leerGRW2("grwave2.out",2) #el numero 2 viene explicado en dicha funcion, solo elimina un fallo que se contemplaba para esta funcion
                ultimo=d_km[-1] #coge el ultimo valor que podrá usarse para calcular la distancia, metiendolo en una variable global
                self.update_graph(d_km,intensidad,color,label) #se llama a la funcion que genera la grafica
        
    def rellenarEntrada(self,HTT,HRR,FREQ,SIGMA,EPSLON,IPOLRN,dmin,dmax,dstep): #Usada en ambas pestañas. Rellena fichero de entrada.dat para GRWAVE
        fentrada = open('entrada.dat', 'w')
        fentrada.write('HTT '+HTT+'\n'+'HRR '+HRR+'\n'+'FREQ '+FREQ+'\n'+'SIGMA '
                       +SIGMA+'\n'+'EPSLON '+EPSLON+'\n'+'IPOLRN '+IPOLRN+'\n'+'dmin '+dmin+'\n'+
                       'dmax '+dmax+'\n'+'dstep '+dstep+'\n'+'GO'+'\n'+'STOP'+'\n')
        fentrada.close() 
                    
    def empezar(self,inicial): #Usada en ambas pestañas
        seguir=ejecucion(self) #hace llamada a GRWAVE
        lecturaSalida(self,inicial) #procesa los datos de salida
        return seguir #notifica si ha habido fallo en llamada a GRWAVE por seleccion de entorno equivocado
        
    def update_graph(self,distancia,intensidad,colorGrafica,etiqueta): #Dibuja gráfica terreno homogéneo
        self.MplWidget.canvas.axes.set_title('Curva de propagación',fontsize=10) #Titulo grafica
        self.MplWidget.canvas.axes.set_xlabel('Distancia [km]',fontsize=8) #Etiqueta eje X
        self.MplWidget.canvas.axes.set_ylabel('Intensidad de campo [dB(µV/m)]',fontsize=8) #Etiqueta eje Y
        self.MplWidget.canvas.axes.set_ylim(-20,120) #Limite superior e inferior de eje Y
        self.MplWidget.canvas.axes.set_xlim(1,10000) #Limite superior e inferior de eje X
        self.MplWidget.canvas.axes.grid(True,which="both",linewidth=0.5) #Activar cuadrícula en ambos ejes con anchura 0.5
        #se introduce en la grafica la curva con valores de distancia e intensidad para cada eje. Las etiquetas y color
        #se pasan por parámetros para diferenciar una curva de otra en la misma grafica
        self.MplWidget.canvas.axes.plot(distancia, intensidad,label=etiqueta,color=colorGrafica,linewidth=1)
        self.MplWidget.canvas.axes.legend(loc='upper right',prop={'size': 7}) #leyenda situada arriba a la derecha, con tamaño de fuente 7.
        self.MplWidget.canvas.axes.semilogx(distancia,intensidad,color=colorGrafica) #aplica escala logaritmica a eje X. Se vuelve a pasar datos de ejes X e Y, y el color.
        self.MplWidget.canvas.draw() #Se dibuja en la gráfica, es decir, se aplican y muestran los cambios.        
        
    def saveFig1(self): #Abre QDialog para guardar archivo seleccionando carpeta, en las extensiones especificadas.
        fileName = QFileDialog.getSaveFileName(self,
            self.tr("Exportar gráfica"),
            "", self.tr("PNG (*.png);;PDF (*.pdf);;EPS (*.eps);;RAW (*.raw);;PGF (*.pgf);; PS (*.ps);;RAW (*.raw);;"
                        "RGBA (*.rgba);;SVG (*.svg);;SVGZ (*.svgz)"))[0]
        if fileName: #si se ha seleccionado el boton Guardar, fileName estara relleno y contiene el nombre del archivo con la extension
            self.MplWidget.canvas.figure.savefig(fileName, dpi=300, quality=80, optimize=True, progressive=True)
    
    def calculaDistancia(self): #calculara el valor de intensidad para distancia introducida una vez generada grafica
        global ultimo #se coge la variable ultimo haciendola global, para usarla en otra funcion
        distancia=self.lineEdit.text() #se toma el texto de la distancia
        if (distancia==""): # se comprueba que no se ha dejado vacio una vez pulsado Calcular, sino, error
            self.lanzarWarning("Es necesario especificar una distancia")
        elif(float(distancia)>ultimo): #se comprueba que la distancia no supera el rango maximo de distancia que se puede obtener
            self.lanzarWarning("Distancia fuera de rango. \n Valor máximo: "+str(ultimo))
        else:
            dmin=distancia #pone el valor que queremos calcular como dmin, que se metera en entrada.dat
            distancia2=float(distancia) #lo convierte a float para realizarle una suma
            dmax=distancia2+1
            dmax2=str(dmax) #distancia+1 se convierte a cadena para introducirse en entrada.dat, ya que en ficheros solo se pueden escribir strings.
            dstep="1" #el salto será solo de 1, es decir, de dmin a dmax solo habra 1 paso, solo 2 valores
            HTT=self.HTT.text()
            HRR=self.HRR.text()
            FREQ=self.FREQ.text()
            SIGMA=self.SIGMA.text()
            EPSLON=self.EPSLON.text()
            if self.Horizontal.isChecked(): #comprueba si esta marcada la polarizacion horizontal
                IPOLRN='2' #el valor 2 es porque GRWAVE entiende 2 como horizontal y 1 como vertical
            elif self.Vertical.isChecked(): #comprueba si es polarizacion vertical
                IPOLRN='1'
            self.rellenarEntrada(HTT,HRR,FREQ,SIGMA,EPSLON,IPOLRN,dmin,dmax2,dstep) #rellena fichero entrada.dat
            seguir=self.empezar(1) #llama a funcion empezar, que ejecutará llamada a GRWAVE y recogerá datos de salida
            if(seguir==True): #no ha habido fallo ejecutando GRWAVE 
                d_km, intensidad,perdidas=leerGRW2("grwave2.out",1) #se recogen los valores de grwave2.out (solo habra 2 pares)
                if (d_km.size==0): #comprobar que no esta vacio, es decir, que no se ha metido un valor demasiado alto o nulo
                    self.lanzarWarning("Distancia fuera de rango")
                    self.lineEdit_2.setText("") #se ponen los campos de E y Lb vacios, para evitar confusiones.
                    self.lineEdit_3.setText("")
                    
                else:
                    self.lineEdit_2.setText(str(intensidad.item(0))) #si todo esta bien, se mete en E y Lb el primer par de valores correspondientes a dmin, que es el valor que queremos
                    self.lineEdit_3.setText(str(perdidas.item(0)))
       
    def clearr(self): #limpia la gráfica homogenea, pero vuelve a asignar valores de configuración de gráfica vacía
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.set_title('Curva de propagación',fontsize=10)
        self.MplWidget.canvas.axes.set_xlabel('Distancia [km]',fontsize=8)
        self.MplWidget.canvas.axes.set_ylabel('Intensidad de campo [dB(µV/m)]',fontsize=8)
        self.MplWidget.canvas.axes.set_ylim(-20,120)
        self.MplWidget.canvas.axes.set_xlim(1,10000)
        self.MplWidget.canvas.axes.grid(True,which="both",linewidth=0.5)
        self.MplWidget.canvas.axes.semilogx()
        self.MplWidget.canvas.draw()
        self.ocultaDistancia() 
        
    def ocultaDistancia(self): #cuando se limpia una grafica, o se selecciona mas de una frecuencia, se desactivan las casillas para calcular la distancia
        self.lineEdit.setReadOnly(True) #Distancia en modo solo lectura, para no admitir que se pueda escribir.
        self.lineEdit.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.lineEdit_2.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.lineEdit_3.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("") 
        
    ##################################################################################
    ##################################################################################
    ##################################################################################
    ##################################################################################
    # FUNCIONES TERRENO MIXTO
    
    def informacion(self): #Abre informacion con la tabla de caracteristicas de terrenos
        self.ventanaInfo=QtWidgets.QMainWindow()
        self.ui=Ui_Info()
        self.ui.setupUi(self.ventanaInfo)
        self.ventanaInfo.setWindowFlags(QtCore.Qt.WindowCloseButtonHint);
        self.ventanaInfo.setWindowIcon(QIcon("iconn.png"))
        self.ventanaInfo.show()
 
    def comprobarWarning_2(self):
        #Se comprueba que ningun parametro introducido esta vacio, a excepcion de los terrenos 3 y 4 que se hara
        #mas adelante
        if(self.HTT_2.text()=="" or self.HRR_2.text()=="" or self.Sigma1.text()=="" 
           or self.Epsilon1.text()=="" or self.Sigma2.text()=="" 
           or self.Epsilon2.text()=="" or self.Long1.text()=="" 
           or self.Long2.text()=="" or self.FREQmixto.text()==""):
            parar=True #si hay alguno vacio, se debe parar la ejecucion
            self.lanzarWarning("Es necesario rellenar todos los campos")#se lanza ventana emergente con error especificado
            
        #Se comprueba que todos los valores introducidos estan en formato float, a excepcion de terrenos 3 y 4
        elif (self.is_float(self.HTT_2.text())==False or self.is_float(self.HRR_2.text())==False or 
              self.is_float(self.Sigma2.text())==False or self.is_float(self.Epsilon1.text())==False or 
              self.is_float(self.Sigma1.text())==False or self.is_float(self.Long1.text())==False or 
              self.is_float(self.Epsilon2.text())==False or self.is_float(self.Long2.text())==False or 
              self.is_float(self.FREQmixto.text())==False):
            parar=True
            self.lanzarWarning("Los parámetros deben ser formato float")
        
        #Se comprueba que la frecuencia esta entre 10 kHz y 30 MHz    
        elif(float(self.FREQmixto.text())>30 or float(self.FREQmixto.text())<0.01):  #se comprueba que la frecuencia esta dentro del rango (10 kHz-30 MHz)
            self.lanzarWarning("La frecuencia debe estar entre \n 10 KHz y 30 MHz")
            parar=True
        else: #si no hay errores, no se para la ejecucion
            parar=False
        return parar
      
    def inhabilitaSigEps1(self): #cuando se ha seleccionado un terreno predeterminado, las casillas de sigma y epsilon se configuran para solo lectura
        self.Sigma1.setReadOnly(True)
        self.Epsilon1.setReadOnly(True)
        self.Sigma1.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.Epsilon1.setStyleSheet("background-color: rgb(235, 235, 235);")
    
    def inhabilitaSigEps2(self): #igual, pero para el terreno 2
        self.Sigma2.setReadOnly(True)
        self.Epsilon2.setReadOnly(True)
        self.Sigma2.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.Epsilon2.setStyleSheet("background-color: rgb(235, 235, 235);")
        
    def inhabilitaSigEps3(self): #igual para terreno 3
        self.Sigma3.setReadOnly(True)
        self.Epsilon3.setReadOnly(True)
        self.Sigma3.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.Epsilon3.setStyleSheet("background-color: rgb(235, 235, 235);")
        
    def inhabilitaSigEps4(self): #igual para terreno 4
        self.Sigma4.setReadOnly(True)
        self.Epsilon4.setReadOnly(True)
        self.Sigma4.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.Epsilon4.setStyleSheet("background-color: rgb(235, 235, 235);")
                                
    def comprobarTerrenos(self):  #numero de terrenos, desplegable 1 2 3 4
        comboText = self.comboBox_3.currentText()            
        if (comboText=="2"): #si el numero de terrenos seleccionados es 2, oculta los parametros y etiquetas de los bloques de terrenos 3 y 4           
            self.label_50.setVisible(False) #Correspondiente al bloque 3
            self.label_51.setVisible(False)
            self.label_52.setVisible(False)
            self.comboBox_6.setVisible(False)
            self.Epsilon3.setVisible(False)
            self.Sigma3.setVisible(False)
            self.Long3.setVisible(False)            
            self.label_53.setVisible(False) #Correspondiente al bloque 4
            self.label_54.setVisible(False)
            self.label_55.setVisible(False)
            self.comboBox_7.setVisible(False)
            self.Epsilon4.setVisible(False)
            self.Sigma4.setVisible(False)
            self.Long4.setVisible(False)
            self.line.setVisible(False)            
        elif (comboText=="3"):            
            self.label_50.setVisible(True) #Correspondiente al bloque 3
            self.label_51.setVisible(True)
            self.label_52.setVisible(True)
            self.comboBox_6.setVisible(True)
            self.Epsilon3.setVisible(True)
            self.Sigma3.setVisible(True)
            self.Long3.setVisible(True)           
            self.label_53.setVisible(False) #Correspondiente al bloque 4
            self.label_54.setVisible(False)
            self.label_55.setVisible(False)
            self.comboBox_7.setVisible(False)
            self.Epsilon4.setVisible(False)
            self.Sigma4.setVisible(False)
            self.Long4.setVisible(False)
            self.line.setVisible(True)            
        elif (comboText=="4"):            
            self.label_50.setVisible(True) #Correspondiente al bloque 3
            self.label_51.setVisible(True)
            self.label_52.setVisible(True)
            self.comboBox_6.setVisible(True)
            self.Epsilon3.setVisible(True)
            self.Sigma3.setVisible(True)
            self.Long3.setVisible(True)           
            self.label_53.setVisible(True) #Correspondiente al bloque 4
            self.label_54.setVisible(True)
            self.label_55.setVisible(True)
            self.comboBox_7.setVisible(True)
            self.Epsilon4.setVisible(True)
            self.Sigma4.setVisible(True)
            self.Long4.setVisible(True)
            self.line.setVisible(True)
            
    def actualizaTerreno1(self): #si en el desplegable de terreno 1 se ha tomado valor predefinido, se actualizan las casillas de sigma y epsilon, poniendo modo lectura si toca
        terreno = self.comboBox_4.currentText()
        if(terreno=="Agua del mar, salinidad baja"):
            self.Sigma1.setText("1")
            self.Epsilon1.setText("80")
            self.inhabilitaSigEps1()         
        elif(terreno=="Agua del mar, salinidad media"):
            self.Sigma1.setText("5")
            self.Epsilon1.setText("70")
            self.inhabilitaSigEps1()
        elif(terreno=="Agua dulce"):
            self.Sigma1.setText("0.003")
            self.Epsilon1.setText("80")
            self.inhabilitaSigEps1()
        elif(terreno=="Tierra"):
            self.Sigma1.setText("0.03")
            self.Epsilon1.setText("40")
            self.inhabilitaSigEps1()
        elif(terreno=="Tierra húmeda"):
            self.Sigma1.setText("0.01")
            self.Epsilon1.setText("30")
            self.inhabilitaSigEps1()
        elif(terreno=="Tierra moderadamente seca"):
            self.Sigma1.setText("0.001")
            self.Epsilon1.setText("15")
            self.inhabilitaSigEps1()
        elif(terreno=="Tierra seca"):
            self.Sigma1.setText("0.0003")
            self.Epsilon1.setText("7")
            self.inhabilitaSigEps1()
        elif(terreno=="Tierra muy seca"):
            self.Sigma1.setText("0.0001")
            self.Epsilon1.setText("3")
            self.inhabilitaSigEps1()
        elif(terreno=="Hielo de agua dulce, -1ºC"):
            self.Sigma1.setText("0.00003")
            self.Epsilon1.setText("3")
            self.inhabilitaSigEps1()
        elif(terreno=="Hielo de agua dulce, -10ºC"):
            self.Sigma1.setText("-0.00001")
            self.Epsilon1.setText("3")
            self.inhabilitaSigEps1()
        elif(terreno=="Personalizado"): #cuando es personalizado, se desactiva modo solo lectura para introducir manualmente los parametros
            self.Sigma1.setText("")
            self.Epsilon1.setText("")
            self.Sigma1.setReadOnly(False)
            self.Epsilon1.setReadOnly(False)
            self.Sigma1.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.Epsilon1.setStyleSheet("background-color: rgb(255, 255, 255);")
            
    def actualizaTerreno2(self):
        terreno = self.comboBox_5.currentText()
        if(terreno=="Agua del mar, salinidad baja"):
            self.Sigma2.setText("1")
            self.Epsilon2.setText("80")
            self.inhabilitaSigEps2()         
        elif(terreno=="Agua del mar, salinidad media"):
            self.Sigma2.setText("5")
            self.Epsilon2.setText("70")
            self.inhabilitaSigEps2()
        elif(terreno=="Agua dulce"):
            self.Sigma2.setText("0.003")
            self.Epsilon2.setText("80")
            self.inhabilitaSigEps2()
        elif(terreno=="Tierra"):
            self.Sigma2.setText("0.03")
            self.Epsilon2.setText("40")
            self.inhabilitaSigEps2()
        elif(terreno=="Tierra húmeda"):
            self.Sigma2.setText("0.01")
            self.Epsilon2.setText("30")
            self.inhabilitaSigEps2()
        elif(terreno=="Tierra moderadamente seca"):
            self.Sigma2.setText("0.001")
            self.Epsilon2.setText("15")
            self.inhabilitaSigEps2()
        elif(terreno=="Tierra seca"):
            self.Sigma2.setText("0.0003")
            self.Epsilon2.setText("7")
            self.inhabilitaSigEps2()
        elif(terreno=="Tierra muy seca"):
            self.Sigma2.setText("0.0001")
            self.Epsilon2.setText("3")
            self.inhabilitaSigEps2()
        elif(terreno=="Hielo de agua dulce, -1ºC"):
            self.Sigma2.setText("0.00003")
            self.Epsilon2.setText("3")
            self.inhabilitaSigEps2()
        elif(terreno=="Hielo de agua dulce, -10ºC"):
            self.Sigma2.setText("-0.00001")
            self.Epsilon2.setText("3")
            self.inhabilitaSigEps2()
        elif(terreno=="Personalizado"):
            self.Sigma2.setText("")
            self.Epsilon2.setText("")
            self.Sigma2.setReadOnly(False)
            self.Epsilon2.setReadOnly(False)
            self.Sigma2.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.Epsilon2.setStyleSheet("background-color: rgb(255, 255, 255);")
            
    def actualizaTerreno3(self):
        terreno = self.comboBox_6.currentText()
        if(terreno=="Agua del mar, salinidad baja"):
            self.Sigma3.setText("1")
            self.Epsilon3.setText("80")
            self.inhabilitaSigEps3()         
        elif(terreno=="Agua del mar, salinidad media"):
            self.Sigma3.setText("5")
            self.Epsilon3.setText("70")
            self.inhabilitaSigEps3()
        elif(terreno=="Agua dulce"):
            self.Sigma3.setText("0.003")
            self.Epsilon3.setText("80")
            self.inhabilitaSigEps3()
        elif(terreno=="Tierra"):
            self.Sigma3.setText("0.03")
            self.Epsilon3.setText("40")
            self.inhabilitaSigEps3()
        elif(terreno=="Tierra húmeda"):
            self.Sigma3.setText("0.01")
            self.Epsilon3.setText("30")
            self.inhabilitaSigEps3()
        elif(terreno=="Tierra moderadamente seca"):
            self.Sigma3.setText("0.001")
            self.Epsilon3.setText("15")
            self.inhabilitaSigEps3()
        elif(terreno=="Tierra seca"):
            self.Sigma3.setText("0.0003")
            self.Epsilon3.setText("7")
            self.inhabilitaSigEps3()
        elif(terreno=="Tierra muy seca"):
            self.Sigma3.setText("0.0001")
            self.Epsilon3.setText("3")
            self.inhabilitaSigEps3()
        elif(terreno=="Hielo de agua dulce, -1ºC"):
            self.Sigma3.setText("0.00003")
            self.Epsilon3.setText("3")
            self.inhabilitaSigEps3()
        elif(terreno=="Hielo de agua dulce, -10ºC"):
            self.Sigma3.setText("-0.00001")
            self.Epsilon3.setText("3")
            self.inhabilitaSigEps3()
        elif(terreno=="Personalizado"):
            self.Sigma3.setText("")
            self.Epsilon3.setText("")
            self.Sigma3.setReadOnly(False)
            self.Epsilon3.setReadOnly(False)
            self.Sigma3.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.Epsilon3.setStyleSheet("background-color: rgb(255, 255, 255);")
            
    def actualizaTerreno4(self):
        terreno = self.comboBox_7.currentText()
        if(terreno=="Agua del mar, salinidad baja"):
            self.Sigma4.setText("1")
            self.Sigma4.setText("80")
            self.inhabilitaSigEps4()         
        elif(terreno=="Agua del mar, salinidad media"):
            self.Sigma4.setText("5")
            self.Epsilon4.setText("70")
            self.inhabilitaSigEps4()
        elif(terreno=="Agua dulce"):
            self.Sigma4.setText("0.003")
            self.Epsilon4.setText("80")
            self.inhabilitaSigEps4()
        elif(terreno=="Tierra"):
            self.Sigma4.setText("0.03")
            self.Epsilon4.setText("40")
            self.inhabilitaSigEps4()
        elif(terreno=="Tierra húmeda"):
            self.Sigma4.setText("0.01")
            self.Epsilon4.setText("30")
            self.inhabilitaSigEps4()
        elif(terreno=="Tierra moderadamente seca"):
            self.Sigma4.setText("0.001")
            self.Epsilon4.setText("15")
            self.inhabilitaSigEps4()
        elif(terreno=="Tierra seca"):
            self.Sigma4.setText("0.0003")
            self.Epsilon4.setText("7")
            self.inhabilitaSigEps4()
        elif(terreno=="Tierra muy seca"):
            self.Sigma4.setText("0.0001")
            self.Epsilon4.setText("3")
            self.inhabilitaSigEps4()
        elif(terreno=="Hielo de agua dulce, -1ºC"):
            self.Sigma4.setText("0.00003")
            self.Epsilon4.setText("3")
            self.inhabilitaSigEps4()
        elif(terreno=="Hielo de agua dulce, -10ºC"):
            self.Sigma4.setText("-0.00001")
            self.Epsilon4.setText("3")
            self.inhabilitaSigEps4()
        elif(terreno=="Personalizado"):
            self.Sigma4.setText("")
            self.Epsilon4.setText("")
            self.Sigma4.setReadOnly(False)
            self.Epsilon4.setReadOnly(False)
            self.Sigma4.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.Epsilon4.setStyleSheet("background-color: rgb(255, 255, 255);")
                                                                
    def secuenciaMixta(self): #se comprueba si el numero de terrenos seleccionado es 2, 3 o 4
        self.clearr_2() #se limpia grafica anterior
        comboText = self.comboBox_3.currentText()
        parar=self.comprobarWarning_2() #comprueba una serie de posibles errores iniciales, parametros incompletos, rango frecuencia, etc.
        if (parar==False): #si todo ha ido bien
            if (comboText=="2"): #si el numero de terrenos es 2
                SIGMA1=self.Sigma1.text() #recoge datos de sigma y epsilon 
                SIGMA2=self.Sigma2.text()
                EPSLON1=self.Epsilon1.text()
                EPSLON2=self.Epsilon2.text()
                Label1='εᵣ='+EPSLON1+', σ='+SIGMA1 #prepara sus etiquetas para la leyenda
                Label2='εᵣ='+EPSLON2+', σ='+SIGMA2
                self.generar_2(SIGMA1,EPSLON1,0,'#0093FF',Label1) #genera sus curvas en la grafica con ciertos colores, el 0 indica que es la primera vez
                self.generar_2(SIGMA2,EPSLON2,1, '#FF9B00',Label2) #el 1 indica que se continue solapando curvas
                Long1=self.Long1.text() #se recogen valores de longitudes y se calculan valores de intensidad en esos puntos siguiendo Metodo Millington
                E1=self.calculaDistancia11(Long1)
                Long2=self.Long2.text()
                Long12=str(float(Long1)+float(Long2))
                E12=self.calculaDistancia22(Long12)
                E2=self.calculaDistancia22(Long1)
                E22=self.calculaDistancia22(Long2)
                E21=self.calculaDistancia11(Long12)
                E11=self.calculaDistancia11(Long2)
                if((E1 is not None) and (E12 is not None) and (E2 is not None) and 
                       (E22 is not None) and (E21 is not None) and (E11 is not None)): #si ningun dato de intensidad de campo electrico esta vacio
                    ED=E1+E12-E2 #sigue las formulas de Metodo Millington, mirar en ITU-R P.368
                    ER=E22+E21-E11
                    ET=(ER+ED)/2
                else:
                    ET=None
                if(ET is not None): #si el campo total ET no esta vacio, se rellena en su sitio, redondeando 2 decimales
                    self.lineEdit_4.setText(str(round(ET,2)))
                else:
                    self.lineEdit_4.setText("") #si estuviera vacio ET, se marca como vacía su casilla
                    
            elif (comboText=="3"): #igual para terreno 3, añadiendo mas variables y usando mas terminos en las formulas de Millington
                #Se comrpueba que los valores del terreno 3 no estan vacios    
                if (self.Epsilon3.text()=="" or self.Sigma3.text()=="" or self.Long3.text()==""):
                    self.lanzarWarning("Es necesario rellenar todos los campos")
                #Se comprueba que los valores del terreno 3 son float
                elif(self.is_float(self.Epsilon3.text())==False or self.is_float(self.Sigma3.text())==False or 
                     self.is_float(self.Long3.text())==False):
                    self.lanzarWarning("Los parámetros deben ser formato float")
                else:
                    SIGMA1=self.Sigma1.text()   #Se recogen los textos de las casillas
                    SIGMA2=self.Sigma2.text()
                    SIGMA3=self.Sigma3.text()
                    EPSLON1=self.Epsilon1.text()
                    EPSLON2=self.Epsilon2.text()
                    EPSLON3=self.Epsilon3.text()
                    Label1='εᵣ='+EPSLON1+', σ='+SIGMA1 #Etiquetas usadas para la leyenda
                    Label2='εᵣ='+EPSLON2+', σ='+SIGMA2
                    Label3='εᵣ='+EPSLON3+', σ='+SIGMA3
                    self.generar_2(SIGMA1,EPSLON1,0,'#0093FF',Label1)
                    self.generar_2(SIGMA2,EPSLON2,0,'#FF9B00',Label2)
                    self.generar_2(SIGMA3,EPSLON3,1,'#60C146',Label3)
                    Long1=self.Long1.text()
                    E1=self.calculaDistancia11(Long1)
                    Long2=self.Long2.text()
                    Long12=str(float(Long1)+float(Long2))
                    Long3=self.Long3.text()
                    Long123=str(float(Long1)+float(Long2)+float(Long3))
                    E33=self.calculaDistancia33(Long123)
                    E12=self.calculaDistancia22(Long12)
                    E2=self.calculaDistancia22(Long1)
                    E32=self.calculaDistancia33(Long12)
                    E31=self.calculaDistancia33(Long3)
                    Long23=str(float(Long2)+float(Long3))
                    E23=self.calculaDistancia22(Long23)
                    E123=self.calculaDistancia11(Long123)
                    E223=self.calculaDistancia22(Long3)
                    E11=self.calculaDistancia11(Long23)
                    if((E1 is not None) and (E12 is not None) and (E33 is not None) and (E2 is not None) and 
                       (E32 is not None) and (E31 is not None) and (E23 is not None) and (E123 is not None) and 
                       (E223 is not None) and (E11 is not None)):
                        ED=E1+E12+E33-E2-E32
                        ER=E31+E23+E123-E223-E11
                        ET=(ER+ED)/2
                    else:
                        ET=None
                    if(ET is not None):
                        self.lineEdit_4.setText(str(round(ET,2)))
                    else:
                        self.lineEdit_4.setText("")
                        
            elif (comboText=="4"):
                #Se comprueba que los valores del terreno 3 y 4 no están vacios
                if (self.Epsilon3.text()=="" or self.Sigma3.text()=="" or self.Long3.text()==""
                    or self.Epsilon4.text()=="" or self.Sigma4.text()=="" or self.Long4.text()==""):
                    self.lanzarWarning("Es necesario rellenar todos los campos")
                #Se comprueba que los valores del terreno 3 y 4 son float
                elif(self.is_float(self.Epsilon3.text())==False or self.is_float(self.Sigma3.text())==False or 
                     self.is_float(self.Long3.text())==False or self.is_float(self.Epsilon4.text())==False 
                     or self.is_float(self.Sigma4.text())==False or self.is_float(self.Long4.text())==False):
                    self.lanzarWarning("Los parámetros deben ser formato float")
                else:
                    SIGMA1=self.Sigma1.text()
                    SIGMA2=self.Sigma2.text()
                    SIGMA3=self.Sigma3.text()
                    SIGMA4=self.Sigma4.text()
                    EPSLON1=self.Epsilon1.text()
                    EPSLON2=self.Epsilon2.text()
                    EPSLON3=self.Epsilon3.text()
                    EPSLON4=self.Epsilon4.text()
                    Label1='εᵣ='+EPSLON1+', σ='+SIGMA1
                    Label2='εᵣ='+EPSLON2+', σ='+SIGMA2
                    Label3='εᵣ='+EPSLON3+', σ='+SIGMA3
                    Label4='εᵣ='+EPSLON4+', σ='+SIGMA4
                    self.generar_2(SIGMA1,EPSLON1,0,'#0093FF',Label1)
                    self.generar_2(SIGMA2,EPSLON2,0,'#FF9B00',Label2)
                    self.generar_2(SIGMA3,EPSLON3,0,'#60C146',Label3)
                    self.generar_2(SIGMA4,EPSLON4,1,'#BE54C7',Label4)
                    Long1=self.Long1.text()
                    E1=self.calculaDistancia11(Long1)
                    Long2=self.Long2.text()
                    Long12=str(float(Long1)+float(Long2))
                    Long3=self.Long3.text()
                    Long4=self.Long4.text()
                    Long123=str(float(Long1)+float(Long2)+float(Long3))
                    Long1234=str(float(Long1)+float(Long2)+float(Long3)+float(Long4))
                    E33=self.calculaDistancia33(Long123)
                    E12=self.calculaDistancia22(Long12)
                    E41234=self.calculaDistancia44(Long1234)
                    E2=self.calculaDistancia22(Long1)
                    E32=self.calculaDistancia33(Long12)
                    E4123=self.calculaDistancia44(Long123)
                    E4=self.calculaDistancia44(Long4)
                    Long34=str(float(Long3)+float(Long4))
                    E334=self.calculaDistancia33(Long34)
                    Long234=str(float(Long2)+float(Long3)+float(Long4))
                    E2234=self.calculaDistancia22(Long234)
                    E11234=self.calculaDistancia11(Long1234)
                    E34=self.calculaDistancia33(Long4)
                    E234=self.calculaDistancia22(Long34)
                    E1234=self.calculaDistancia11(Long234)
                    if((E1 is not None) and (E12 is not None) and (E33 is not None) and (E41234 is not None) and 
                       (E2 is not None) and (E32 is not None) and (E4123 is not None) and (E4 is not None) and 
                       (E334 is not None) and (E2234 is not None) and (E11234 is not None) and (E34 is not None) and 
                       (E234 is not None) and (E1234 is not None)):
                        ED=E1+E12+E33+E41234-E2-E32-E4123
                        ER=E4+E334+E2234+E11234-E34-E234-E1234
                        ET=(ER+ED)/2
                    else:
                        ET=None
                    if(ET is not None):
                        self.lineEdit_4.setText(str(round(ET,2)))
                    else:
                        self.lineEdit_4.setText("")
        
    def generar_2(self,SIGMA,EPSLON,calcular,color,label):
        HTT=self.HTT_2.text()#recoge textos de los parametros introducidos
        HRR=self.HRR_2.text()
        FREQ=self.FREQmixto.text()
        if self.Horizontal_2.isChecked():
            IPOLRN='2'  #Para GRWAVE, 2 es horizontal y 1 es vertical en el parametro IPOLRN
        elif self.Vertical_2.isChecked():
            IPOLRN='1'
        #Se itera durante 4 veces. Cada curva será consecuencia de 4 llamadas a GRWAVE. Para que la escala logaritmica del eje X, segmentada en 4 divisiones, tenga en cada
            #una de ellas los mismos puntos (100), se ha hecho eso. Cada uno tiene un dstep distinto para asegurar que hay 100 puntos en cada division.
        for i in [0, 1, 2, 3]:
            if i==0:
                dmin='1'
                dmax='10'
                dstep='0.1'
                inicial=1;
            elif i==1:
                dmin='10'
                dmax='100'
                dstep='1'
                inicial=0;
            elif i==2:
                dmin='100'
                dmax='1000'
                dstep='10'
                inicial=0;
            elif i==3:
                dmin='1000'
                dmax='10000'
                dstep='100'
                inicial=0;
            self.rellenarEntrada(HTT,HRR,FREQ,SIGMA,EPSLON,IPOLRN,dmin,dmax,dstep) #se rellena fichero de entrada para GRWAVE, entrada.dat
            seguir=self.empezar(inicial)  #realiza llamada a grwave y recoge datos de salida. Variable SEGUIR indica si ha habido fallo en la seleccion del entorno Windows o MSDOS.
        if(seguir==True): #no ha habido fallo ejecutando GRWAVE     
            d_km, intensidad,perdidas=leerGRW2("grwave2.out",2)#el numero 2 viene explicado en dicha funcion, solo elimina un fallo que se contemplaba para esta funcion
            self.update_graph_2(d_km,intensidad,color,label)  #se llama a la funcion que genera la grafica
            if (calcular==1): #si el valor de longitud total es valido, se calcula la intensidad recibida
                comboText = self.comboBox_3.currentText() #coge valor del desplegable de terrenos
                if (comboText=="2"): #indica para cuantos terrenos se calcula, en este caso combinacion de 2
                    Distancia1=self.Long1.text() #coge variables de longitudes
                    Distancia2=self.Long2.text()
                elif(comboText=="3"):
                    Distancia1=self.Long1.text()
                    Distancia2=self.Long2.text()
                    Distancia3=self.Long3.text()
                elif(comboText=="4"):
                    Distancia1=self.Long1.text()
                    Distancia2=self.Long2.text()
                    Distancia3=self.Long3.text()
                    Distancia4=self.Long4.text()
        
    def update_graph_2(self,distancia,intensidad,colorGrafica,etiqueta): #Dibuja gráfica terreno mixto
        self.MplWidget_2.canvas.axes.set_title('Curva de propagación',fontsize=10) #Titulo grafica
        self.MplWidget_2.canvas.axes.set_xlabel('Distancia [km]',fontsize=8) #Etiqueta eje X
        self.MplWidget_2.canvas.axes.set_ylabel('Intensidad de campo [dB(µV/m)]',fontsize=8) #Etiqueta eje Y
        self.MplWidget_2.canvas.axes.set_ylim(-20,120) #Limite superior e inferior de eje Y
        self.MplWidget_2.canvas.axes.set_xlim(1,10000) #Limite superior e inferior de eje X
        self.MplWidget_2.canvas.axes.grid(True,which="both",linewidth=0.5) #Activar cuadrícula en ambos ejes con anchura 0.5
        #se introduce en la grafica la curva con valores de distancia e intensidad para cada eje. Las etiquetas y color
        #se pasan por parámetros para diferenciar una curva de otra en la misma grafica
        self.MplWidget_2.canvas.axes.plot(distancia, intensidad,label=etiqueta,color=colorGrafica)
        self.MplWidget_2.canvas.axes.legend(loc='upper right',prop={'size': 8})#leyenda situada arriba a la derecha, con tamaño de fuente 7.
        self.MplWidget_2.canvas.axes.semilogx(distancia,intensidad,color=colorGrafica)#aplica escala logaritmica a eje X. Se vuelve a pasar datos de ejes X e Y, y el color.
        self.MplWidget_2.canvas.draw() #Se dibuja en la gráfica, es decir, se aplican y muestran los cambios.
        
    def clearr_2(self): #limpia la gráfica mixta, pero vuelve a asignar valores de configuración de gráfica vacía
        self.MplWidget_2.canvas.axes.clear()
        self.MplWidget_2.canvas.axes.set_title('Curva de propagación',fontsize=10)
        self.MplWidget_2.canvas.axes.set_xlabel('Distancia [km]',fontsize=8)
        self.MplWidget_2.canvas.axes.set_ylabel('Intensidad de campo [dB(µV/m)]',fontsize=8)
        self.MplWidget_2.canvas.axes.set_ylim(-20,120)
        self.MplWidget_2.canvas.axes.set_xlim(1,10000)
        self.MplWidget_2.canvas.axes.grid(True,which="both",linewidth=0.5)
        self.MplWidget_2.canvas.axes.semilogx()
        self.MplWidget_2.canvas.draw()
        self.lineEdit_4.setText("")            
      
    def saveFig2(self): #Abre QDialog para guardar archivo seleccionando carpeta, en las extensiones especificadas.
        fileName = QFileDialog.getSaveFileName(self,
            self.tr("Exportar gráfica"),
            "", self.tr("PNG (*.png);;PDF (*.pdf);;EPS (*.eps);;RAW (*.raw);;PGF (*.pgf);; PS (*.ps);;RAW (*.raw);;"
                        "RGBA (*.rgba);;SVG (*.svg);;SVGZ (*.svgz)"))[0]
        if fileName: #si se ha seleccionado el boton Guardar, fileName estara relleno y contiene el nombre del archivo con la extension
            self.MplWidget_2.canvas.figure.savefig(fileName, dpi=300, quality=80, optimize=True, progressive=True)
             
    def calculaDistancia11(self,distancia): #calcula intensidad de campo electrico segun metodo millington con datos del terreno 1, a la distancia que se le marque por parametro
        if(float(distancia)>10000): #La grafica y GRWAVE solo llega a 10000, si es mayor se descarta
            self.lanzarWarning('Suma de distancias fuera de rango'+'\n'+'Imposible calcular E')
            self.lineEdit_4.setText("") #Se rellena vacio el resultado del campo, para borrar el resultado anterior
        else: #Se llama a GRWAVE pero solo usando el terreno 1
            dmin=distancia
            distancia2=float(distancia)
            dmax=distancia2+1
            dmax2=str(dmax)
            dstep="1"
            HTT=self.HTT_2.text()
            HRR=self.HRR_2.text()
            FREQ=self.FREQmixto.text()
            SIGMA=self.Sigma1.text()
            EPSLON=self.Epsilon1.text()
            if self.Horizontal_2.isChecked():
                IPOLRN='2'
            elif self.Vertical_2.isChecked():
                IPOLRN='1'
            self.rellenarEntrada(HTT,HRR,FREQ,SIGMA,EPSLON,IPOLRN,dmin,dmax2,dstep)
            seguir=self.empezar(1)
            if(seguir==True): #no ha habido fallo ejecutando GRWAVE 
                d_km, intensidad,perdidas=leerGRW2("grwave2.out",1)
                if (d_km.size==0): #Solo debe devolver un valor el del campo para esa distancia. Si su tamaño es 0, error
                    self.lanzarWarning('Suma de distancias fuera de rango'+'\n'+'Imposible calcular E')
                    self.lineEdit_4.setText("")
                else:
                    return intensidad.item(0)
        
    def calculaDistancia22(self,distancia): #calcula intensidad de campo electrico segun metodo millington con datos del terreno 2, a la distancia que se le marque por parametro
        if(float(distancia)>10000): 
            self.lanzarWarning('Suma de distancias fuera de rango'+'\n'+'Imposible calcular E')
            self.lineEdit_4.setText("")
        else: #Se llama a GRWAVE pero solo usando el terreno 2
            dmin=distancia
            distancia2=float(distancia)
            dmax=distancia2+1
            dmax2=str(dmax)
            dstep="1"
            HTT=self.HTT_2.text()
            HRR=self.HRR_2.text()
            FREQ=self.FREQmixto.text()
            SIGMA=self.Sigma2.text()
            EPSLON=self.Epsilon2.text()
            if self.Horizontal_2.isChecked():
                IPOLRN='2'
            elif self.Vertical_2.isChecked():
                IPOLRN='1'
            self.rellenarEntrada(HTT,HRR,FREQ,SIGMA,EPSLON,IPOLRN,dmin,dmax2,dstep)
            seguir=self.empezar(1)
            if(seguir==True): #no ha habido fallo ejecutando GRWAVE 
                d_km, intensidad,perdidas=leerGRW2("grwave2.out",1)
                if (d_km.size==0): #Solo debe devolver un valor el del campo para esa distancia. Si su tamaño es 0, error
                    self.lanzarWarning('Suma de distancias fuera de rango'+'\n'+'Imposible calcular E')
                    self.lineEdit_4.setText("")
                else:
                    return intensidad.item(0)
        
    def calculaDistancia33(self,distancia): #para datos del terreno 3
        if(float(distancia)>10000):
            self.lanzarWarning('Suma de distancias fuera de rango'+'\n'+'Imposible calcular E')
            self.lineEdit_4.setText("")
        else: #Se llama a GRWAVE pero solo usando el terreno 3
            dmin=distancia
            distancia2=float(distancia)
            dmax=distancia2+1
            dmax2=str(dmax)
            dstep="1"
            HTT=self.HTT_2.text()
            HRR=self.HRR_2.text()
            FREQ=self.FREQmixto.text()
            SIGMA=self.Sigma3.text()
            EPSLON=self.Epsilon3.text()
            if self.Horizontal_2.isChecked():
                IPOLRN='2'
            elif self.Vertical_2.isChecked():
                IPOLRN='1'
            self.rellenarEntrada(HTT,HRR,FREQ,SIGMA,EPSLON,IPOLRN,dmin,dmax2,dstep)
            seguir=self.empezar(1)
            if(seguir==True): #no ha habido fallo ejecutando GRWAVE 
                d_km, intensidad,perdidas=leerGRW2("grwave2.out",1)
                if (d_km.size==0): #Solo debe devolver un valor el del campo para esa distancia. Si su tamaño es 0, error
                    self.lanzarWarning('Suma de distancias fuera de rango'+'\n'+'Imposible calcular E')
                    self.lineEdit_4.setText("")
                else:
                    return intensidad.item(0)
        
    def calculaDistancia44(self,distancia): #para datos del terreno 4
        if(float(distancia)>10000): 
            self.lanzarWarning('Suma de distancias fuera de rango'+'\n'+'Imposible calcular E')
            self.lineEdit_4.setText("")
        else: #Se llama a GRWAVE pero solo usando el terreno 4
            dmin=distancia
            distancia2=float(distancia)
            dmax=distancia2+1
            dmax2=str(dmax)
            dstep="1"
            HTT=self.HTT_2.text()
            HRR=self.HRR_2.text()
            FREQ=self.FREQmixto.text()
            SIGMA=self.Sigma4.text()
            EPSLON=self.Epsilon4.text()
            if self.Horizontal_2.isChecked():
                IPOLRN='2'
            elif self.Vertical_2.isChecked():
                IPOLRN='1'
            self.rellenarEntrada(HTT,HRR,FREQ,SIGMA,EPSLON,IPOLRN,dmin,dmax2,dstep)
            seguir=self.empezar(1)
            if(seguir==True): #no ha habido fallo ejecutando GRWAVE 
                d_km, intensidad,perdidas=leerGRW2("grwave2.out",1)
                if (d_km.size==0): #Solo debe devolver un valor el del campo para esa distancia. Si su tamaño es 0, error
                    self.lanzarWarning('Suma de distancias fuera de rango'+'\n'+'Imposible calcular E')
                    self.lineEdit_4.setText("")
                else:
                    return intensidad.item(0)
               
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.setWindowIcon(QtGui.QIcon('iconn.ico'))
    window.setWindowIcon(QtGui.QIcon('iconn.ico'))
    app.exec_()