# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       interruptorPalanca.py
# Autores:      Miguel Andres Garcia Niño - Ángel Iván Hernández
# Creado:       29 de Junio 2018
# Modificado:   29 de Junio 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño - Ángel Iván Hernández, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *interruptorPalanca* tiene como objetivo imitar las funciones de un
Toggle Switch (Interruptor de palanca).
"""

# Versión Python: 3.5.2
# Versión PyQt5: 5.10.0

from PyQt5.QtGui import QIcon, QFont, QPalette, QColor, QPixmap
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QTimer, QPropertyAnimation, QAbstractAnimation
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QFrame, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from ventanaCalculos import *
import os

# ========================= CLASE Frame ===========================

class Frame(QFrame):
    clicked = pyqtSignal(str)
    MIN_VALOR = 1
    MAX_VALOR = 121
    VALOR = MAX_VALOR + MIN_VALOR
    
    def __init__(self, parent=None):
        super(Frame, self).__init__(parent)
        self.parent = parent
        self.mover = QPoint()
        self.habilitado = False

    def actualizarEstado(self):
        # Si la posicion x del boton mas la mitad de su ancho
        # es menor que la mitad del ancho del widget padre,
        # entonces esta apagado (NO)
        if (self.parent.button.x() + (self.parent.button.width() / 2)) < Frame.VALOR / 2:
            self.habilitado = False            
        # Si la posicion x del boton mas la mitad de su ancho
        # es mayor que la mitad del ancho del widget padre,
        # entonces esta encendido (SI)
        if (self.parent.button.x() + (self.parent.button.width() / 2)) > Frame.VALOR / 2:
            self.habilitado = True
            
        if self.habilitado:
            self.parent.button.setText("MSDOS")
            color = QColor(250, 185, 78)
        elif not self.habilitado:
            self.parent.button.setText("Windows")
            color = QColor(78, 172, 250)

        colorFrame = self.palette()
        colorFrame.setColor(QPalette.Background, color)
        self.setPalette(colorFrame)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mover.setY(1)            
            if event.pos().x() < Frame.VALOR / 2:
                self.mover.setX(Frame.MIN_VALOR)
            elif event.pos().x() > Frame.VALOR / 2:
                self.mover.setX(Frame.MAX_VALOR - self.parent.button.width())

            self.animacion = QPropertyAnimation(self.parent.button, b"pos")
            self.animacion.setDuration(150)
            self.animacion.setEndValue(self.mover)
            self.animacion.valueChanged.connect(self.actualizarEstado)
            self.animacion.finished.connect(self.emitirEstado)
            self.animacion.start(QAbstractAnimation.DeleteWhenStopped)

    def emitirEstado(self):
        self.clicked.emit(self.parent.button.text())
        
# ====================== CLASE PushButton =========================

class PushButton(QPushButton):
    clicked = pyqtSignal(str)
    
    MIN_VALOR = 1
    MAX_VALOR = 121
    VALOR = MAX_VALOR + MIN_VALOR
    
    def __init__(self, parent=None):
        super(PushButton, self).__init__(parent)
        self.parent = parent        
        self.pressing = False
        self.inicio = QPoint()
        self.mover = QPoint()
        self.habilitado = False
        self.arrastrado = False
        
        self.actualizarEstado()
        self.actualizarPosicion()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.ultimo = True
            self.inicio = event.pos()
            self.pressing = True
            self.actualizarEstado()

    def actualizarEstado(self):
        # Si la posicion x del boton mas la mitad de su ancho
        # es menor que la mitad del ancho del widget padre,
        # entonces esta apagado (NO)
        if (self.x() + (self.width() / 2)) < PushButton.VALOR / 2:
            self.habilitado = False
            
        # Si la posicion x del boton mas la mitad de su ancho
        # es mayor que la mitad del ancho del widget padre,
        # entonces esta encendido (SI)
        if (self.x() + (self.width() / 2)) > PushButton.VALOR / 2:
            self.habilitado = True
            
        if self.habilitado:
            self.setText("MSDOS")
            color = QColor(250, 185, 78)
        elif not self.habilitado:
            self.setText("Windows")
            color = QColor(78, 172, 250)

        colorFrame = self.palette()
        colorFrame.setColor(QPalette.Background, color)
        self.parent.setPalette(colorFrame)

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.mover = self.mapToParent(event.pos() - self.inicio)
            self.mover.setY(1)
            self.move(self.mover)
            self.arrastrado = True
            self.restringirMovimiento()
            self.actualizarEstado()

    def actualizarPosicion(self):
        self.mover.setY(1)
        if self.habilitado:
            self.mover.setX(PushButton.MAX_VALOR - self.width())
        else:
            self.mover.setX(PushButton.MIN_VALOR)

        self.animacion = QPropertyAnimation(self, b"pos")
        self.animacion.setDuration(150)
        self.animacion.setEndValue(self.mover)
        self.animacion.finished.connect(self.emitirEstado)
        self.animacion.start(QAbstractAnimation.DeleteWhenStopped)

    def restringirMovimiento(self):
        self.mover.setY(1)
        
        # Restringir lado izquierdo
        if self.x() < PushButton.MIN_VALOR:
            self.mover.setX(PushButton.MIN_VALOR)
            self.move(self.mover)
            return
        
        # Restringir lado derecho
        if (self.x() + self.width()) > PushButton.MAX_VALOR:
            self.mover.setX(PushButton.MAX_VALOR - self.width())
            self.move(self.mover)
            return

    def mouseReleaseEvent(self, event):
        if self.pressing:
            self.pressing = False
            self.actualizarEstado()
            self.actualizarPosicion()

            if not self.arrastrado and self.ultimo:
                # QApplication.instance().doubleClickInterval()
                QTimer.singleShot(100, self.performSingleClickAction)
            else:
                self.arrastrado = False

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.ultimo = False
    
    def performSingleClickAction(self):
        if self.ultimo:
            self.mover.setY(1)
            if self.habilitado:
                self.mover.setX(PushButton.MIN_VALOR)
            else:
                self.mover.setX(PushButton.MAX_VALOR - self.width())

            self.animacion = QPropertyAnimation(self, b"pos")
            self.animacion.setDuration(150)
            self.animacion.setEndValue(self.mover)
            self.animacion.valueChanged.connect(self.actualizarEstado)
            self.animacion.finished.connect(self.emitirEstado)
            self.animacion.start(QAbstractAnimation.DeleteWhenStopped)

    def emitirEstado(self):
        self.clicked.emit(self.text())

# =================== CLASE interruptorPalanca ====================

class interruptorPalanca(QDialog):
    def __init__(self, parent=None):
        super(interruptorPalanca, self).__init__(parent)
        self.setWindowIcon(QIcon("iconn.png"))
        self.setWindowTitle("GroundWave Simulator")
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        #self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(867, 604)
        self.initUI()

    def initUI(self):
      # ========================= WIDGETS =========================

        fuenteLabel = self.font()
        fuenteLabel.setBold(True)
        fuenteLabel.setFamily("Bahnschrift Light")
        fuenteLabel.setPointSize(10)

        self.frame = Frame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFixedSize(122, 32)
        self.frame.setAutoFillBackground(True)
        self.frame.move(370, 334)
        
        self.button = PushButton(self.frame)
        self.button.setFixedSize(64, 30)
        self.button.setAutoDefault(False)
        self.button.move(1, 1)

        self.labelEstado = QLabel("El simulador se ejecutará en: Windows", self)
        self.labelTitulo = QLabel(self)
        self.labelTitulo.setGeometry(QtCore.QRect(0, 40, 865, 111))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(28)
        self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
        
        self.label_2 = QLabel("Desarrollado para la representación y determinación de intensidad de campo eléctrico recibido \n"
"por onda de superficie para frecuencias entre 10 kHZ y 30 MHz según la Rec. ITU-R P.368-9.",self)
        self.label_2.setGeometry(QtCore.QRect(0, 153, 861, 61))
        #font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(146, 146, 146);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.labelEstado.setFont(fuenteLabel)
        self.labelEstado.move(304, 373)
        self.labelEstado.setStyleSheet("color: rgb(53, 53, 53);")
        
        self.label_3 = QLabel("Elige ejecutar el simulador en el terminal de Windows, o en MSDOS mediante el emulador DOSBox:",self)
        self.label_3.setGeometry(QtCore.QRect(0, 290, 861, 41))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(146, 146, 146);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        
        pixmap = QPixmap('Logo2.png')
        self.labelTitulo.setPixmap(pixmap)
        
        buttoon=QPushButton("Empezar",self)
        buttoon.setGeometry(QtCore.QRect(365, 460, 131, 35))
        buttoon.setObjectName("botoncito")
        #♣self.Empezar = PushButton("Empezar")
        #self.Empezar.move(304, 363)
        buttoon.setStyleSheet("#botoncito {\n"
"        border: 1px solid;\n"
"        background-color: rgb(0, 200, 60);\n"
"        color: #FFF;\n"
"        font-weight: bolder;\n"
"        border-color: rgb(65, 65, 65);\n"
"        font-family: \'Roboto\';\n"
"        font-size: 17px;\n"
"    }"
                      "#botoncito:hover {\n"
"    background-color: rgb(16, 214, 96);\n"
"    }"
                      )
    
        buttonGUIA = QPushButton("Abrir",self)
        buttonGUIA.setGeometry(QtCore.QRect(785, 570, 55, 21))
        buttonGUIA.setObjectName("buttonGUIA")
        buttonGUIA.setStyleSheet("color: rgb(80,80,80)")
            
        self.mail = QLabel(self)
        self.mail.setGeometry(QtCore.QRect(20, 565, 30, 30))
        pixmail = QPixmap('mail.png')
        self.mail.setPixmap(pixmail)
        
        self.labelMail = QLabel("javojepri@alum.us.es",self)
        self.labelMail.setGeometry(QtCore.QRect(52, 563, 361, 31))
        self.labelMail.setFont(font)
        self.labelMail.setStyleSheet("color: rgb(146, 146, 146);")
        
        self.labelInfo = QLabel("Para más información, consulta la guía:",self)
        self.labelInfo.setAlignment(QtCore.Qt.AlignRight)
        self.labelInfo.setGeometry(QtCore.QRect(477, 571, 301, 31))
        self.labelInfo.setFont(font)
        self.labelInfo.setStyleSheet("color: rgb(146, 146, 146);")
        
        self.etsi = QLabel(self)
        self.etsi.setGeometry(QtCore.QRect(2, 490, 200, 77))
        pixetsi = QPixmap('etsi.png')
        self.etsi.setPixmap(pixetsi)

      # =============== EVENTOS QFRAME - QPUSHBUTTON ==============

        self.frame.clicked.connect(self.estadoInterruptor)
        self.button.clicked.connect(self.estadoInterruptor)
        buttoon.clicked.connect(self.openWindow)
        buttonGUIA.clicked.connect(self.openGuia)

  # ======================== FUNCIONES ============================

    def estadoInterruptor(self, texto):
        self.labelEstado.setText("El simulador se ejecutará en: {}".format(texto))

    def openWindow(self):
        ui=MainWindow(self)
        ui.show()
        
    def openGuia(self):
        os.startfile("Guia.txt")

# =================================================================

if __name__ == '__main__':
    import sys
    aplicacion = QApplication(sys.argv)
    ventana = interruptorPalanca()
    ventana.show()
    sys.exit(aplicacion.exec_())