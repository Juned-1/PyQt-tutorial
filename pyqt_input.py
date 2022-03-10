#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 18:39:05 2021

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
        my_label = qtw.QLabel("Hello,Enter Your Name")
        #Putting label in screen
        self.layout().addWidget(my_label)
        #If we want to change the shape, size of font that is part of QtGui, not QtWidget, even though label is widget
        #Change the size of label
        my_label.setFont(qtg.QFont('Helvetica',18))
        #creatintg an inpit box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field") #creating object name for input box because we may later need reference to this object
        my_entry.setText("Please enter your name here")
        self.layout().addWidget(my_entry)
        #Create a button
        my_button = qtw.QPushButton("Press Me!", 
        clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        #Show the app
        self.show()
        #function defination of clicking button
        def press_it():
            #Add name to label
            my_label.setText(f"Hello {my_entry.text()}!") #f_string begin with f, it is used to create a formatted string
            my_entry.setText("") #Setting box empty after taking string rom it
            #Clear the input box
app = qtw.QApplication([])
mw = MainWindow()
#Run the app
app.exec_() #exec_ is execute function in pyQt