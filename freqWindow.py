# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popUpWarning.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_Freq(object):
    def setupUi(self, popUp):
        popUp.setObjectName("popUpFreq")
        popUp.resize(316, 189)
        popUp.setStyleSheet("    #popUp2{\n"
"        background-color: rgb(255, 255, 255);\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(popUp)
        self.centralwidget.setObjectName("centralwidget")
        self.freqLabel = QtWidgets.QLabel(self.centralwidget)
        self.freqLabel.setGeometry(QtCore.QRect(0, 0, 316, 179))
        self.freqLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.freqLabel.setText("El cálculo de una curva se realiza con \n un único valor de frecuencia, con lo cual, \n"
                               "la selección de múltiples frecuencias \ngenerará varias curvas independientes. \n \n"
                               "Es posible que la ejecución de una gráfica \n con más de una distinción contenga retardo. \n \n"
                               "El uso de frecuencias está restringido \n para el rango entre 10 kHz y 30 MHz.")
        popUp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(popUp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 271, 21))
        self.menubar.setObjectName("menubar")
        popUp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(popUp)
        self.statusbar.setObjectName("statusbar")
        popUp.setStatusBar(self.statusbar)

        self.retranslateUi(popUp)
        QtCore.QMetaObject.connectSlotsByName(popUp)

    def retranslateUi(self, popUp):
        _translate = QtCore.QCoreApplication.translate
        popUp.setWindowTitle(_translate("popUpFreq", "Información sobre frecuencias"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    popUp = QtWidgets.QMainWindow()
    ui = Ui_Freq()
    ui.setupUi(popUp)
    popUp.show()
    sys.exit(app.exec_())