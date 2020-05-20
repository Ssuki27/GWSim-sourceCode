# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 00:52:36 2020

@author: Usuario
"""
import sys
from popUpWarning import Ui_popUp

class GUIForm(Ui_popUp):
    def __init__(self, parent=None):
        Ui_popUp.__init__(self, parent)
        self.threadData()

    def closeEvent(self, event):
        print ("User has clicked the red x on the main window")
        event.accept()


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    myapp = GUIForm()
    myapp.show()
    ret = app.exec_()
    sys.exit(ret)