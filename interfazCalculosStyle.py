# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

## Archivo .py transformado de un .ui que genera QtDesigner. Facilita el diseño y estilo de la interfaz.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(867, 604)
        MainWindow.setMinimumSize(QtCore.QSize(867, 604))
        MainWindow.setMaximumSize(QtCore.QSize(867, 604))
        MainWindow.setStyleSheet("/*Cambiamos el color de la ventana*/\n"
"    #MainWindow{\n"
"        background-color: rgb(255, 255, 255);\n"
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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 861, 581))
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid;\n"
"    border-color:  rgb(65, 65, 65);\n"
"    background: white;\n"
"}\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid;\n"
"    border-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(34, 34, 34);\n"
"    color: white;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: white;\n"
"    color:  rgb(34, 34, 34);\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background:rgb(232, 232, 232);\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.button_limpiar = QtWidgets.QPushButton(self.tab)
        self.button_limpiar.setGeometry(QtCore.QRect(420, 370, 101, 31))
        self.button_limpiar.setObjectName("button_limpiar")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 281, 51))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(210, 20, 61, 21))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 191, 22))
        self.comboBox.setStyleSheet("backgroundr: white;")
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 200, 141, 16))
        self.label_7.setObjectName("label_7")
        self.Vertical = QtWidgets.QRadioButton(self.tab)
        self.Vertical.setGeometry(QtCore.QRect(131, 80, 91, 16))
        self.Vertical.setChecked(True)
        self.Vertical.setObjectName("Vertical")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(560, 310, 241, 141))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(10, 50, 61, 20))
        self.label_14.setObjectName("label_14")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 110, 71, 23))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 50, 81, 20))
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.label_13.setObjectName("label_13")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 81, 21))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 80, 81, 20))
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setGeometry(QtCore.QRect(10, 80, 61, 20))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_2)
        self.label_28.setGeometry(QtCore.QRect(170, 20, 31, 21))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.groupBox_2)
        self.label_29.setGeometry(QtCore.QRect(170, 50, 61, 21))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        self.label_30.setGeometry(QtCore.QRect(170, 80, 31, 21))
        self.label_30.setObjectName("label_30")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 171, 16))
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(250, 200, 41, 21))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.button_iniciar = QtWidgets.QPushButton(self.tab)
        self.button_iniciar.setGeometry(QtCore.QRect(420, 320, 101, 31))
        self.button_iniciar.setObjectName("button_iniciar")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(250, 20, 41, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(250, 50, 41, 21))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 151, 16))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 81, 16))
        self.label_5.setObjectName("label_5")
        self.Horizontal = QtWidgets.QRadioButton(self.tab)
        self.Horizontal.setGeometry(QtCore.QRect(210, 80, 82, 17))
        self.Horizontal.setObjectName("Horizontal")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 171, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 230, 281, 291))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(240, 50, 41, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 121, 16))
        self.label_4.setObjectName("label_4")
        self.FREQ = QtWidgets.QLineEdit(self.groupBox_3)
        self.FREQ.setGeometry(QtCore.QRect(170, 50, 71, 20))
        self.FREQ.setStyleSheet("")
        self.FREQ.setObjectName("FREQ")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 20, 61, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 80, 121, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(240, 80, 41, 21))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(10, 110, 121, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(240, 140, 41, 21))
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(240, 110, 41, 21))
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(10, 140, 121, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setGeometry(QtCore.QRect(10, 170, 121, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(240, 200, 41, 21))
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(240, 170, 41, 21))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(240, 260, 41, 21))
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(10, 200, 121, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_3)
        self.label_24.setGeometry(QtCore.QRect(10, 260, 121, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox_3)
        self.label_25.setGeometry(QtCore.QRect(240, 230, 41, 21))
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_3)
        self.label_26.setGeometry(QtCore.QRect(10, 230, 121, 16))
        self.label_26.setObjectName("label_26")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 20, 61, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.FREQ_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.FREQ_2.setGeometry(QtCore.QRect(170, 80, 71, 20))
        self.FREQ_2.setStyleSheet("")
        self.FREQ_2.setObjectName("FREQ_2")
        self.FREQ_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.FREQ_3.setGeometry(QtCore.QRect(170, 110, 71, 20))
        self.FREQ_3.setStyleSheet("")
        self.FREQ_3.setObjectName("FREQ_3")
        self.FREQ_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.FREQ_4.setGeometry(QtCore.QRect(170, 140, 71, 20))
        self.FREQ_4.setStyleSheet("")
        self.FREQ_4.setObjectName("FREQ_4")
        self.FREQ_5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.FREQ_5.setGeometry(QtCore.QRect(170, 170, 71, 20))
        self.FREQ_5.setStyleSheet("")
        self.FREQ_5.setObjectName("FREQ_5")
        self.FREQ_6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.FREQ_6.setGeometry(QtCore.QRect(170, 200, 71, 20))
        self.FREQ_6.setStyleSheet("")
        self.FREQ_6.setObjectName("FREQ_6")
        self.FREQ_7 = QtWidgets.QLineEdit(self.groupBox_3)
        self.FREQ_7.setGeometry(QtCore.QRect(170, 230, 71, 20))
        self.FREQ_7.setStyleSheet("")
        self.FREQ_7.setObjectName("FREQ_7")
        self.FREQ_8 = QtWidgets.QLineEdit(self.groupBox_3)
        self.FREQ_8.setGeometry(QtCore.QRect(170, 260, 71, 20))
        self.FREQ_8.setStyleSheet("")
        self.FREQ_8.setObjectName("FREQ_8")
        self.button_exportar = QtWidgets.QPushButton(self.tab)
        self.button_exportar.setGeometry(QtCore.QRect(420, 420, 101, 31))
        self.button_exportar.setObjectName("button_exportar")
        self.HTT = QtWidgets.QLineEdit(self.tab)
        self.HTT.setGeometry(QtCore.QRect(180, 20, 71, 20))
        self.HTT.setObjectName("HTT")
        self.HRR = QtWidgets.QLineEdit(self.tab)
        self.HRR.setGeometry(QtCore.QRect(180, 50, 71, 20))
        self.HRR.setObjectName("HRR")
        self.EPSLON = QtWidgets.QLineEdit(self.tab)
        self.EPSLON.setGeometry(QtCore.QRect(180, 170, 71, 20))
        self.EPSLON.setObjectName("EPSLON")
        self.SIGMA = QtWidgets.QLineEdit(self.tab)
        self.SIGMA.setGeometry(QtCore.QRect(180, 200, 71, 20))
        self.SIGMA.setObjectName("SIGMA")
        self.MplWidget = MplWidget(self.tab)
        self.MplWidget.setGeometry(QtCore.QRect(320, 0, 541, 281))
        self.MplWidget.setStyleSheet("background-color:white;")
        self.MplWidget.setObjectName("MplWidget")
        self.button_cerrar = QtWidgets.QPushButton(self.tab)
        self.button_cerrar.setGeometry(QtCore.QRect(700, 490, 101, 31))
        self.button_cerrar.setObjectName("button_cerrar")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_31 = QtWidgets.QLabel(self.tab_2)
        self.label_31.setGeometry(QtCore.QRect(250, 20, 41, 21))
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.Vertical_2 = QtWidgets.QRadioButton(self.tab_2)
        self.Vertical_2.setGeometry(QtCore.QRect(131, 80, 91, 16))
        self.Vertical_2.setChecked(True)
        self.Vertical_2.setObjectName("Vertical_2")
        self.label_32 = QtWidgets.QLabel(self.tab_2)
        self.label_32.setGeometry(QtCore.QRect(20, 80, 81, 16))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.tab_2)
        self.label_33.setGeometry(QtCore.QRect(250, 50, 41, 21))
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.HTT_2 = QtWidgets.QLineEdit(self.tab_2)
        self.HTT_2.setGeometry(QtCore.QRect(180, 20, 71, 20))
        self.HTT_2.setObjectName("HTT_2")
        self.label_34 = QtWidgets.QLabel(self.tab_2)
        self.label_34.setGeometry(QtCore.QRect(20, 50, 121, 16))
        self.label_34.setObjectName("label_34")
        self.Horizontal_2 = QtWidgets.QRadioButton(self.tab_2)
        self.Horizontal_2.setGeometry(QtCore.QRect(210, 80, 82, 17))
        self.Horizontal_2.setObjectName("Horizontal_2")
        self.label_35 = QtWidgets.QLabel(self.tab_2)
        self.label_35.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.tab_2)
        self.label_36.setGeometry(QtCore.QRect(20, 110, 121, 16))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.tab_2)
        self.label_37.setGeometry(QtCore.QRect(250, 110, 41, 21))
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.MplWidget_2 = MplWidget(self.tab_2)
        self.MplWidget_2.setGeometry(QtCore.QRect(320, 0, 541, 281))
        self.MplWidget_2.setStyleSheet("background-color:white;")
        self.MplWidget_2.setObjectName("MplWidget_2")
        self.button_cerrar_2 = QtWidgets.QPushButton(self.tab_2)
        self.button_cerrar_2.setGeometry(QtCore.QRect(700, 490, 101, 31))
        self.button_cerrar_2.setObjectName("button_cerrar_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(560, 310, 241, 61))
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_38 = QtWidgets.QLabel(self.groupBox_4)
        self.label_38.setGeometry(QtCore.QRect(80, 30, 81, 20))
        self.label_38.setObjectName("label_38")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 30, 61, 20))
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.button_exportar_2 = QtWidgets.QPushButton(self.tab_2)
        self.button_exportar_2.setGeometry(QtCore.QRect(420, 420, 101, 31))
        self.button_exportar_2.setObjectName("button_exportar_2")
        self.button_limpiar_2 = QtWidgets.QPushButton(self.tab_2)
        self.button_limpiar_2.setGeometry(QtCore.QRect(420, 370, 101, 31))
        self.button_limpiar_2.setObjectName("button_limpiar_2")
        self.button_iniciar_2 = QtWidgets.QPushButton(self.tab_2)
        self.button_iniciar_2.setGeometry(QtCore.QRect(420, 320, 101, 31))
        self.button_iniciar_2.setObjectName("button_iniciar_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 140, 281, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 20, 61, 22))
        self.comboBox_3.setStyleSheet("backgroundr: white;")
        self.comboBox_3.setDuplicatesEnabled(False)
        self.comboBox_3.setFrame(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_7.setGeometry(QtCore.QRect(160, 20, 111, 21))
        self.pushButton_7.setObjectName("pushButton_7")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 200, 281, 331))
        self.groupBox_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_6.setFlat(False)
        self.groupBox_6.setCheckable(False)
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_44 = QtWidgets.QLabel(self.groupBox_6)
        self.label_44.setGeometry(QtCore.QRect(210, 10, 61, 20))
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.groupBox_6)
        self.label_45.setGeometry(QtCore.QRect(160, 10, 41, 20))
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.groupBox_6)
        self.label_46.setGeometry(QtCore.QRect(120, 60, 81, 21))
        self.label_46.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 30, 141, 22))
        self.comboBox_4.setStyleSheet("backgroundr: white;")
        self.comboBox_4.setDuplicatesEnabled(False)
        self.comboBox_4.setFrame(True)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_47 = QtWidgets.QLabel(self.groupBox_6)
        self.label_47.setGeometry(QtCore.QRect(160, 90, 41, 20))
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.groupBox_6)
        self.label_48.setGeometry(QtCore.QRect(210, 90, 61, 20))
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_5.setGeometry(QtCore.QRect(10, 110, 141, 22))
        self.comboBox_5.setStyleSheet("backgroundr: white;")
        self.comboBox_5.setDuplicatesEnabled(False)
        self.comboBox_5.setFrame(True)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_49 = QtWidgets.QLabel(self.groupBox_6)
        self.label_49.setGeometry(QtCore.QRect(120, 140, 81, 21))
        self.label_49.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.groupBox_6)
        self.label_50.setGeometry(QtCore.QRect(160, 170, 41, 20))
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.groupBox_6)
        self.label_51.setGeometry(QtCore.QRect(210, 170, 61, 20))
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_6.setGeometry(QtCore.QRect(10, 190, 141, 22))
        self.comboBox_6.setStyleSheet("backgroundr: white;")
        self.comboBox_6.setDuplicatesEnabled(False)
        self.comboBox_6.setFrame(True)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_52 = QtWidgets.QLabel(self.groupBox_6)
        self.label_52.setGeometry(QtCore.QRect(120, 220, 81, 21))
        self.label_52.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.groupBox_6)
        self.label_53.setGeometry(QtCore.QRect(120, 300, 81, 21))
        self.label_53.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.groupBox_6)
        self.label_54.setGeometry(QtCore.QRect(210, 250, 61, 20))
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_7.setGeometry(QtCore.QRect(10, 270, 141, 22))
        self.comboBox_7.setStyleSheet("backgroundr: white;")
        self.comboBox_7.setDuplicatesEnabled(False)
        self.comboBox_7.setFrame(True)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.label_55 = QtWidgets.QLabel(self.groupBox_6)
        self.label_55.setGeometry(QtCore.QRect(160, 250, 41, 20))
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.line = QtWidgets.QFrame(self.groupBox_6)
        self.line.setGeometry(QtCore.QRect(0, 240, 281, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox_6)
        self.line_2.setGeometry(QtCore.QRect(0, 160, 281, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.groupBox_6)
        self.line_3.setGeometry(QtCore.QRect(0, 80, 281, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Epsilon1 = QtWidgets.QLineEdit(self.groupBox_6)
        self.Epsilon1.setGeometry(QtCore.QRect(160, 30, 41, 20))
        self.Epsilon1.setObjectName("Epsilon1")
        self.Sigma1 = QtWidgets.QLineEdit(self.groupBox_6)
        self.Sigma1.setGeometry(QtCore.QRect(210, 30, 61, 20))
        self.Sigma1.setObjectName("Sigma1")
        self.Long1 = QtWidgets.QLineEdit(self.groupBox_6)
        self.Long1.setGeometry(QtCore.QRect(210, 60, 61, 20))
        self.Long1.setObjectName("Long1")
        self.Epsilon2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.Epsilon2.setGeometry(QtCore.QRect(160, 110, 41, 20))
        self.Epsilon2.setObjectName("Epsilon2")
        self.Sigma2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.Sigma2.setGeometry(QtCore.QRect(210, 110, 61, 20))
        self.Sigma2.setObjectName("Sigma2")
        self.Long2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.Long2.setGeometry(QtCore.QRect(210, 140, 61, 20))
        self.Long2.setObjectName("Long2")
        self.Epsilon3 = QtWidgets.QLineEdit(self.groupBox_6)
        self.Epsilon3.setGeometry(QtCore.QRect(160, 190, 41, 20))
        self.Epsilon3.setObjectName("Epsilon3")
        self.Sigma3 = QtWidgets.QLineEdit(self.groupBox_6)
        self.Sigma3.setGeometry(QtCore.QRect(210, 190, 61, 20))
        self.Sigma3.setObjectName("Sigma3")
        self.Long3 = QtWidgets.QLineEdit(self.groupBox_6)
        self.Long3.setGeometry(QtCore.QRect(210, 220, 61, 20))
        self.Long3.setObjectName("Long3")
        self.Epsilon4 = QtWidgets.QLineEdit(self.groupBox_6)
        self.Epsilon4.setGeometry(QtCore.QRect(160, 270, 41, 20))
        self.Epsilon4.setObjectName("Epsilon4")
        self.Sigma4 = QtWidgets.QLineEdit(self.groupBox_6)
        self.Sigma4.setGeometry(QtCore.QRect(210, 270, 61, 20))
        self.Sigma4.setObjectName("Sigma4")
        self.Long4 = QtWidgets.QLineEdit(self.groupBox_6)
        self.Long4.setGeometry(QtCore.QRect(210, 300, 61, 20))
        self.Long4.setObjectName("Long4")
        self.HRR_2 = QtWidgets.QLineEdit(self.tab_2)
        self.HRR_2.setGeometry(QtCore.QRect(180, 50, 71, 20))
        self.HRR_2.setObjectName("HRR_2")
        self.FREQmixto = QtWidgets.QLineEdit(self.tab_2)
        self.FREQmixto.setGeometry(QtCore.QRect(180, 110, 71, 20))
        self.FREQmixto.setObjectName("FREQmixto")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 867, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.MplWidget.setGeometry(QtCore.QRect(320, 0, 541, 309)) #SUSTITUCION
        self.MplWidget_2.setGeometry(QtCore.QRect(320, 0, 541, 309)) #SUSTITUCION
        self.button_iniciar.setIcon(QtGui.QIcon("media2.png"))  #INCRUSTADO
        self.button_iniciar.setIconSize(QtCore.QSize(20,20))    #INCRUSTADO
        self.button_limpiar.setIcon(QtGui.QIcon("goma.png"))    #INCRUSTADO
        self.button_limpiar.setIconSize(QtCore.QSize(20,20))    #INCRUSTADO
        self.button_exportar.setIcon(QtGui.QIcon("export.png"))    #INCRUSTADO
        self.button_exportar.setIconSize(QtCore.QSize(15,15))    #INCRUSTADO
        self.button_cerrar.setIcon(QtGui.QIcon("back.png"))    #INCRUSTADO
        self.button_cerrar.setIconSize(QtCore.QSize(20,20))    #INCRUSTADO
        
        self.button_iniciar_2.setIcon(QtGui.QIcon("media2.png"))  #INCRUSTADO
        self.button_iniciar_2.setIconSize(QtCore.QSize(20,20))    #INCRUSTADO
        self.button_limpiar_2.setIcon(QtGui.QIcon("goma.png"))    #INCRUSTADO
        self.button_limpiar_2.setIconSize(QtCore.QSize(20,20))    #INCRUSTADO
        self.button_exportar_2.setIcon(QtGui.QIcon("export.png"))    #INCRUSTADO
        self.button_exportar_2.setIconSize(QtCore.QSize(15,15))    #INCRUSTADO
        self.button_cerrar_2.setIcon(QtGui.QIcon("back.png"))    #INCRUSTADO
        self.button_cerrar_2.setIconSize(QtCore.QSize(20,20))    #INCRUSTADO
        
        
        self.MplWidget.canvas.axes.set_title('Curva de propagación',fontsize=10)#INCRUSTADO
        self.MplWidget.canvas.axes.set_xlabel('Distancia [km]',fontsize=8)#INCRUSTADO
        self.MplWidget.canvas.axes.set_ylabel('Intensidad de campo [dB(µV/m)]',fontsize=8)#INCRUSTADO
        self.MplWidget.canvas.axes.set_ylim(-20,120)        #INCRUSTADO
        self.MplWidget.canvas.axes.semilogx()           #INCRUSTADO
        self.MplWidget.canvas.axes.set_xlim(1,10000)        #INCRUSTADO
        self.MplWidget.canvas.axes.grid(True,which="both",linewidth=0.5)           #INCRUSTADO
        self.MplWidget_2.canvas.axes.set_title('Curva de propagación',fontsize=10)#INCRUSTADO
        self.MplWidget_2.canvas.axes.set_xlabel('Distancia [km]',fontsize=8)#INCRUSTADO
        self.MplWidget_2.canvas.axes.set_ylabel('Intensidad de campo [dB(µV/m)]',fontsize=8)#INCRUSTADO
        self.MplWidget_2.canvas.axes.set_ylim(-20,120)        #INCRUSTADO
        self.MplWidget_2.canvas.axes.semilogx()           #INCRUSTADO
        self.MplWidget_2.canvas.axes.set_xlim(1,10000)        #INCRUSTADO
        self.MplWidget_2.canvas.axes.grid(True,which="both",linewidth=0.5)           #INCRUSTADO
        self.FREQ_2.setVisible(False)                       #INCRUSTADO
        self.FREQ_3.setVisible(False)                       #INCRUSTADO
        self.FREQ_4.setVisible(False)                       #INCRUSTADO
        self.FREQ_5.setVisible(False)                       #INCRUSTADO
        self.FREQ_6.setVisible(False)                       #INCRUSTADO
        self.FREQ_7.setVisible(False)                       #INCRUSTADO
        self.FREQ_8.setVisible(False)                       #INCRUSTADO
        self.label_11.setVisible(False)                       #INCRUSTADO
        self.label_12.setVisible(False)                       #INCRUSTADO
        self.label_15.setVisible(False)                       #INCRUSTADO
        self.label_16.setVisible(False)                       #INCRUSTADO
        self.label_17.setVisible(False)                       #INCRUSTADO
        self.label_18.setVisible(False)                       #INCRUSTADO
        self.label_19.setVisible(False)                       #INCRUSTADO
        self.label_20.setVisible(False)                       #INCRUSTADO
        self.label_21.setVisible(False)                       #INCRUSTADO
        self.label_22.setVisible(False)                       #INCRUSTADO
        self.label_23.setVisible(False)                       #INCRUSTADO
        self.label_24.setVisible(False)                       #INCRUSTADO
        self.label_25.setVisible(False)                       #INCRUSTADO
        self.label_26.setVisible(False)                       #INCRUSTADO
        self.lineEdit.setReadOnly(True)                       #INCRUSTADO
        self.lineEdit_4.setReadOnly(True)                       #INCRUSTADO
        self.lineEdit.setStyleSheet("background-color: rgb(235, 235, 235);")#INCRUSTADO
        self.lineEdit_2.setStyleSheet("background-color: rgb(235, 235, 235);")#INCRUSTADO
        self.lineEdit_3.setStyleSheet("background-color: rgb(235, 235, 235);")#INCRUSTADO
             
        self.label_50.setVisible(False)                       #INCRUSTADO
        self.label_51.setVisible(False)                       #INCRUSTADO
        self.label_52.setVisible(False)                       #INCRUSTADO
        self.comboBox_6.setVisible(False)                       #INCRUSTADO
        self.Epsilon3.setVisible(False)                       #INCRUSTADO
        self.Sigma3.setVisible(False)                       #INCRUSTADO
        self.Long3.setVisible(False)                       #INCRUSTADO
                
        self.label_53.setVisible(False)                       #INCRUSTADO
        self.label_54.setVisible(False)                       #INCRUSTADO
        self.label_55.setVisible(False)                       #INCRUSTADO
        self.comboBox_7.setVisible(False)                       #INCRUSTADO
        self.Epsilon4.setVisible(False)                       #INCRUSTADO
        self.Sigma4.setVisible(False)                       #INCRUSTADO
        self.Long4.setVisible(False)                       #INCRUSTADO
        self.line.setVisible(False)                       #INCRUSTADO

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GroundWave Simulator"))
        self.button_limpiar.setText(_translate("MainWindow", "Limpiar"))
        self.groupBox.setTitle(_translate("MainWindow", "Elegir tipo de terreno"))
        self.pushButton.setText(_translate("MainWindow", "Ayuda"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Personalizado"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Agua del mar, salinidad baja"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Agua del mar, salinidad media"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Agua dulce"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Tierra"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Tierra húmeda"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Tierra moderadamente seca"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Tierra seca"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Tierra muy seca"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Hielo de agua dulce, -1ºC"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Hielo de agua dulce, -10ºC"))
        self.label_7.setText(_translate("MainWindow", "σ  (Conductividad)"))
        self.Vertical.setText(_translate("MainWindow", "Vertical"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Calcular intensidad de campo eléctrico"))
        self.label_14.setText(_translate("MainWindow", "E"))
        self.pushButton_2.setText(_translate("MainWindow", "Calcular"))
        self.label_13.setText(_translate("MainWindow", "Distancia"))
        self.label_27.setText(_translate("MainWindow", "Lb"))
        self.label_28.setText(_translate("MainWindow", "km"))
        self.label_29.setText(_translate("MainWindow", "dB(µV/m)"))
        self.label_30.setText(_translate("MainWindow", "dB"))
        self.label_3.setText(_translate("MainWindow", "Altura antena receptora"))
        self.label_10.setText(_translate("MainWindow", "S/m"))
        self.button_iniciar.setText(_translate("MainWindow", "Ejecutar"))
        self.label.setText(_translate("MainWindow", "m"))
        self.label_8.setText(_translate("MainWindow", "m"))
        self.label_6.setText(_translate("MainWindow", "εᵣ  (Constante dieléctrica)"))
        self.label_5.setText(_translate("MainWindow", "Polarización"))
        self.Horizontal.setText(_translate("MainWindow", "Horizontal"))
        self.label_2.setText(_translate("MainWindow", "Altura antena transmisora"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Número de frecuencias"))
        self.label_9.setText(_translate("MainWindow", "MHz"))
        self.label_4.setText(_translate("MainWindow", "Frecuencia 1"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "6"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "7"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "8"))
        self.label_11.setText(_translate("MainWindow", "Frecuencia 2"))
        self.label_12.setText(_translate("MainWindow", "MHz"))
        self.label_15.setText(_translate("MainWindow", "Frecuencia 3"))
        self.label_16.setText(_translate("MainWindow", "MHz"))
        self.label_17.setText(_translate("MainWindow", "MHz"))
        self.label_18.setText(_translate("MainWindow", "Frecuencia 4"))
        self.label_19.setText(_translate("MainWindow", "Frecuencia 5"))
        self.label_20.setText(_translate("MainWindow", "MHz"))
        self.label_21.setText(_translate("MainWindow", "MHz"))
        self.label_22.setText(_translate("MainWindow", "MHz"))
        self.label_23.setText(_translate("MainWindow", "Frecuencia 6"))
        self.label_24.setText(_translate("MainWindow", "Frecuencia 8"))
        self.label_25.setText(_translate("MainWindow", "MHz"))
        self.label_26.setText(_translate("MainWindow", "Frecuencia 7"))
        self.pushButton_3.setText(_translate("MainWindow", "Ayuda"))
        self.button_exportar.setText(_translate("MainWindow", "Exportar"))
        self.button_cerrar.setText(_translate("MainWindow", "Regresar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Terreno homogéneo"))
        self.label_31.setText(_translate("MainWindow", "m"))
        self.Vertical_2.setText(_translate("MainWindow", "Vertical"))
        self.label_32.setText(_translate("MainWindow", "Polarización"))
        self.label_33.setText(_translate("MainWindow", "m"))
        self.label_34.setText(_translate("MainWindow", "Altura antena receptora"))
        self.Horizontal_2.setText(_translate("MainWindow", "Horizontal"))
        self.label_35.setText(_translate("MainWindow", "Altura antena transmisora"))
        self.label_36.setText(_translate("MainWindow", "Frecuencia"))
        self.label_37.setText(_translate("MainWindow", "MHz"))
        self.button_cerrar_2.setText(_translate("MainWindow", "Regresar"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Intensidad de campo eléctrico recibido"))
        self.label_38.setText(_translate("MainWindow", "E [dB(µV/m)]"))
        self.button_exportar_2.setText(_translate("MainWindow", "Exportar"))
        self.button_limpiar_2.setText(_translate("MainWindow", "Limpiar"))
        self.button_iniciar_2.setText(_translate("MainWindow", "Ejecutar"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Elegir número de terrenos"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "2"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "3"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "4"))
        self.pushButton_7.setText(_translate("MainWindow", "Información"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Parámetros de cada terreno"))
        self.label_44.setText(_translate("MainWindow", "σ  [S/m]"))
        self.label_45.setText(_translate("MainWindow", "εᵣ"))
        self.label_46.setText(_translate("MainWindow", "Longitud [km]"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Personalizado"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Agua del mar, salinidad baja"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Agua del mar, salinidad media"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Agua dulce"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Tierra"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "Tierra húmeda"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "Tierra moderadamente seca"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "Tierra seca"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "Tierra muy seca"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "Hielo de agua dulce, -1ºC"))
        self.comboBox_4.setItemText(10, _translate("MainWindow", "Hielo de agua dulce, -10ºC"))
        self.label_47.setText(_translate("MainWindow", "εᵣ"))
        self.label_48.setText(_translate("MainWindow", "σ  [S/m]"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Personalizado"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Agua del mar, salinidad baja"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Agua del mar, salinidad media"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "Agua dulce"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "Tierra"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "Tierra húmeda"))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "Tierra moderadamente seca"))
        self.comboBox_5.setItemText(7, _translate("MainWindow", "Tierra seca"))
        self.comboBox_5.setItemText(8, _translate("MainWindow", "Tierra muy seca"))
        self.comboBox_5.setItemText(9, _translate("MainWindow", "Hielo de agua dulce, -1ºC"))
        self.comboBox_5.setItemText(10, _translate("MainWindow", "Hielo de agua dulce, -10ºC"))
        self.label_49.setText(_translate("MainWindow", "Longitud [km]"))
        self.label_50.setText(_translate("MainWindow", "εᵣ"))
        self.label_51.setText(_translate("MainWindow", "σ  [S/m]"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Personalizado"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "Agua del mar, salinidad baja"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Agua del mar, salinidad media"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "Agua dulce"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "Tierra"))
        self.comboBox_6.setItemText(5, _translate("MainWindow", "Tierra húmeda"))
        self.comboBox_6.setItemText(6, _translate("MainWindow", "Tierra moderadamente seca"))
        self.comboBox_6.setItemText(7, _translate("MainWindow", "Tierra seca"))
        self.comboBox_6.setItemText(8, _translate("MainWindow", "Tierra muy seca"))
        self.comboBox_6.setItemText(9, _translate("MainWindow", "Hielo de agua dulce, -1ºC"))
        self.comboBox_6.setItemText(10, _translate("MainWindow", "Hielo de agua dulce, -10ºC"))
        self.label_52.setText(_translate("MainWindow", "Longitud [km]"))
        self.label_53.setText(_translate("MainWindow", "Longitud [km]"))
        self.label_54.setText(_translate("MainWindow", "σ  [S/m]"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Personalizado"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Agua del mar, salinidad baja"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "Agua del mar, salinidad media"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "Agua dulce"))
        self.comboBox_7.setItemText(4, _translate("MainWindow", "Tierra"))
        self.comboBox_7.setItemText(5, _translate("MainWindow", "Tierra húmeda"))
        self.comboBox_7.setItemText(6, _translate("MainWindow", "Tierra moderadamente seca"))
        self.comboBox_7.setItemText(7, _translate("MainWindow", "Tierra seca"))
        self.comboBox_7.setItemText(8, _translate("MainWindow", "Tierra muy seca"))
        self.comboBox_7.setItemText(9, _translate("MainWindow", "Hielo de agua dulce, -1ºC"))
        self.comboBox_7.setItemText(10, _translate("MainWindow", "Hielo de agua dulce, -10ºC"))
        self.label_55.setText(_translate("MainWindow", "εᵣ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Terreno mixto"))
from mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
