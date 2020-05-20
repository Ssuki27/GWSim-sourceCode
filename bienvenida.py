# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bienvenida.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 604)
        MainWindow.setMinimumSize(QtCore.QSize(867, 604))
        MainWindow.setMaximumSize(QtCore.QSize(867, 604))
        MainWindow.setStyleSheet("/*Cambiamos el color de la ventana*/\n"
"    #MainWindow{\n"
"        background-color: rgb(245, 245, 245);\n"
"    }\n"
"\n"
"    /*Estilos para el botón*/\n"
"    #button_iniciar, #button_iniciar_2{\n"
"        border: 1px solid;\n"
"        background-color: rgb(0, 200, 60);\n"
"        color: #fff;\n"
"        border-color: rgb(65, 65, 65);\n"
"        font-family: \'Roboto\';\n"
"        font-size: 17px;\n"
"    }\n"
"    \n"
"    /*Definimos el estilo para un efecto hover sobre el botón,\n"
"    este cambiará su background cuando pasemos el mouse por\n"
"    encima*/\n"
"    #button_iniciar:hover, #button_iniciar_2:hover{\n"
"    background-color: rgb(16, 214, 96);\n"
"    }\n"
"\n"
"\n"
"    /*Definimos los estilos para los QLineEdit*/\n"
"    QLineEdit{\n"
"        border: 1px solid;\n"
"        border-color: rgb(150,150, 150);\n"
"    }\n"
"\n"
"    /*Definimos los estilos para los QLabel*/\n"
"    QLabel{\n"
"        font-family: \'Roboto\';\n"
"    }\n"
"\n"
"    /*Definimos los estilos para los QLabels cuyos nombres son\n"
"    \'label_usuario\' y \'label-password\'*/\n"
"    #label_usuario, #label_password{\n"
"        font-size: 17px;\n"
"        color: #212121;\n"
"    }\n"
"    \n"
"    /*Estilo para el QLable cuyo nombre es #label_login*/\n"
"    #label_login{\n"
"        font-size:30px;\n"
"        color: #fff;\n"
"    }\n"
"\n"
"    #button_limpiar, #button_limpiar_2{\n"
"        border: 1px solid;\n"
"        background-color: rgb(239, 239, 239);\n"
"        color: rgb(65, 65, 65);\n"
"        border-color: rgb(65, 65, 65);\n"
"        font-family: \'Roboto\';\n"
"        font-size: 17px;\n"
"    }\n"
"    #button_limpiar:hover,#button_limpiar_2:hover{\n"
"    background-color: rgb(209, 209, 209);\n"
"    }\n"
"\n"
"    #button_exportar,#button_exportar_2{\n"
"        border: 1px solid;\n"
"        background-color: rgb(239, 239, 239);\n"
"        color: rgb(65, 65, 65);\n"
"        border-color: rgb(65, 65, 65);\n"
"        font-family: \'Roboto\';\n"
"        font-size: 17px;\n"
"    }\n"
"    #button_exportar:hover, #button_exportar_2:hover{\n"
"    background-color: rgb(209, 209, 209);\n"
"    }\n"
"\n"
"    QGroupBox {\n"
"    border: 1px solid;\n"
"    border-color: rgb(166, 166, 166);\n"
"    margin-top: 0.5em;\n"
"    }\n"
"\n"
"    QGroupBox::title {\n"
"    top: -6px;\n"
"    left: 10px;\n"
"    }\n"
"    #button_cerrar, #button_cerrar_2{\n"
"        border: 1px solid;\n"
"        background-color: rgb(239, 239, 239);\n"
"        color: rgb(65, 65, 65);\n"
"        border-color: rgb(223, 22, 22);\n"
"        font-family: \'Roboto\';\n"
"        font-size: 17px;\n"
"    }\n"
"    #button_cerrar:hover,#button_cerrar_2:hover{\n"
"    background-color: rgb(209, 209, 209);\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 40, 861, 111))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(53, 53, 53);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 130, 861, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(146, 146, 146);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulador GRWAVE"))
        self.label.setText(_translate("MainWindow", "GroundWave Simulator"))
        self.label_2.setText(_translate("MainWindow", "Este programa ha sido desarrollado para la representación y determinación de intensidad de campo eléctrico recibida por \n"
" onda de superficie para frecuencias entre 10 kHZ y 30 MHz según la Rec. ITU-R P.368-9"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
