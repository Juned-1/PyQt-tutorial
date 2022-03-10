#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 18:20:47 2021

@author: junaid
"""

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #Add a title to app
        self.setWindowTitle("Hello World")
        #Set Layout
        #vertical box layout
        self.setLayout(qtw.QVBoxLayout()) #It is vertical box layout, for horizontal box layout QHBoxLayout is used
        #Create a Label
        my_label = qtw.QLabel("Hello Mr. Junaid Ahmed Laskar!")
        #Putting label in screen
        self.layout().addWidget(my_label)
        #If we want to change the shape, size of font that is part of QtGui, not QtWidget, even though label is widget
        #Change the size of label
        my_label.setFont(qtg.QFont('Helvetica',18))
        self.show() #show function show our project
app = qtw.QApplication([])
mw = MainWindow()
#Run the app
app.exec_() #exec_ is execute function in pyQt