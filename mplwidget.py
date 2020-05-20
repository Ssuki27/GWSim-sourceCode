# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:04:59 2020

@author: Javier Ojeda Prieto
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import*
from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

    
class MplWidget(QWidget):
    
    def __init__(self, parent = None):

        QWidget.__init__(self, parent)
        
        self.canvas = FigureCanvas(Figure())
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        
        self.canvas.axes = self.canvas.figure.add_subplot(111,position=[0.15, 0.17, 0.75, 0.75])
        self.setLayout(vertical_layout)
        