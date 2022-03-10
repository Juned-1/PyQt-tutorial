#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 10:30:17 2021

@author: junaid
"""

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setLayout(qtw.QVBoxLayout()) 
        my_label = qtw.QLabel("Pick something from the list below")
        self.layout().addWidget(my_label)
        my_label.setFont(qtg.QFont('Helvetica',18))
        #Create Combo box
        my_combo = qtw.QComboBox(self,
                    editable=True,
                    insertPolicy=qtw.QComboBox.InsertAtTop) #If don't pass anything, we can pass self, even if don't pass, there is nothing wrong
        #We can pass editable as true to make it editable combo box
        #Also set insert policy to where new editable item should add
        #If we pass nothing or just, then by default it is not editable
        #We can change insert policy from top, bottom, before and after etc
        #Add item to the combo box
        my_combo.addItem("Pepperoni", "Something")
        my_combo.addItem("Cheese", 2)
        my_combo.addItem("Mushroom", qtw.QWidget)
        my_combo.addItem("Peppers")
        #We can add several item together by addItems
        my_combo.addItems(["One","Two","Three"])
        #insert element in specific position using insertItem(index,item)
        my_combo.insertItem(2,"New thing")
        my_combo.insertItems(4, ["Hello","Hi"])
        #There is also a insertItems() available to insert more than one item once
        #Put Combo in screen
        self.layout().addWidget(my_combo)
        my_button = qtw.QPushButton("Press Me!", 
        clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        self.show()
        def press_it():
            my_label.setText(f"You pick {my_combo.currentText()}!")
            #We can return currentText(), which return current text of item selected from combo
            #We can also return currentData,the second thing passed in combo is data
            #We can also return currentIndex, return index of element in combo
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()