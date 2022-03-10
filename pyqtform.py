#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 11:15:23 2021

@author: junaid
"""
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        #Create a form 
        form_layout = qtw.QFormLayout()
        #We creating s variable now and passing it
        self.setLayout(form_layout)
        
        #Add the stuf like widget button etc in the form
        label1 = qtw.QLabel("This is cool Label Row") #everything in qform layout is our row
        label1.setFont(qtg.QFont("Helvetica", 24))
        
        firstName = qtw.QLineEdit(self)
        lastName = qtw.QLineEdit(self)
        
        #Add Rows to App
        form_layout.addRow(label1)
        form_layout.addRow("First Name",firstName)
        form_layout.addRow("Last Name",lastName)
        form_layout.addRow(qtw.QPushButton("Press me!",
                        clicked = lambda: press_it()))
        #Notice that we have created name, label externally because we need to refernce them late
        #but buuton we do not need to  refer later, so created directly in row and passed refernce
        self.show()
        def press_it():
            label1.setText(f"You clicked  the button, {firstName.text()} {lastName.text()}!")
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()