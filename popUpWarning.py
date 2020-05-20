# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popUpWarning.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_popUp(object):
    def setupUi(self, popUp):
        popUp.setObjectName("popUp")
        popUp.resize(271, 112)
        popUp.setStyleSheet("    #popUp{\n"
"        background-color: rgb(255, 255, 255);\n"
"    }")
        self.centralwidget = QtWidgets.QWidget(popUp)
        self.centralwidget.setObjectName("centralwidget")
        self.labelError = QtWidgets.QLabel(self.centralwidget)
        self.labelError.setGeometry(QtCore.QRect(10, 40, 251, 41))
        self.labelError.setAlignment(QtCore.Qt.AlignCenter)
        self.labelError.setObjectName("labelError")
        self.iconWarning = QtWidgets.QLabel(self.centralwidget)
        self.iconWarning.setGeometry(QtCore.QRect(120, 10, 31, 31))
        self.iconWarning.setText("")
        self.iconWarning.setPixmap(QtGui.QPixmap("warning.png"))
        self.iconWarning.setScaledContents(True)
        self.iconWarning.setObjectName("iconWarning")
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
        popUp.setWindowTitle(_translate("popUp", "Warning"))
        self.labelError.setText(_translate("popUp", "Distancia fuera de rango"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    popUp = QtWidgets.QMainWindow()
    ui = Ui_popUp()
    ui.setupUi(popUp)
    popUp.show()
    sys.exit(app.exec_())
