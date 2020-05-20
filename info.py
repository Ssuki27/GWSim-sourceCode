# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popUpWarning.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_Info(object):
    def setupUi(self, popUp):
        popUp.setObjectName("popUp2")
        popUp.resize(546, 249)
        popUp.setStyleSheet("    #popUp2{\n"
"        background-color: rgb(255, 255, 255);\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(popUp)
        self.centralwidget.setObjectName("centralwidget")
        self.iconWarning = QtWidgets.QLabel(self.centralwidget)
        self.iconWarning.setGeometry(QtCore.QRect(0, 0, 546, 232))
        self.iconWarning.setText("")
        self.iconWarning.setPixmap(QtGui.QPixmap("TablaTerrenos.png"))
        self.iconWarning.setScaledContents(True)
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
        popUp.setWindowTitle(_translate("popUp2", "Características de los terrenos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    popUp = QtWidgets.QMainWindow()
    ui = Ui_Info()
    ui.setupUi(popUp)
    popUp.show()
    sys.exit(app.exec_())