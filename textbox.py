#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 10:37:00 2021

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
        #Create Text box
        my_text = qtw.QTextEdit(self,
                    #plainText = "hi",
                    #html = "<h1>Hello</h1>",
                    acceptRichText = True,
                    lineWrapMode = qtw.QTextEdit.FixedColumnWidth,
                    lineWrapColumnOrWidth = 50,
                    placeholderText = "Enter text here!",
                    readOnly = False,
                    
                    )
        #lineWrapMode set to FixedColumnWidth to fixe the size of text box
        #to box, lineWrapColumnOrWidth set width of the text inside tex box, does not change size of text box just set how far the text will go
        #50 character in one line than wrap to next line
        #by default readOnly is false, you can explicitly mention if you want to
        #acceptRichText will accept Formatted text, like text from world with bold italic etc
        #when it is set True, when  it is false it don't accept richtext
        #We can also set plain textv to box by default by usin plain Text
        #We can also use html in this box, html = ""
        self.layout().addWidget(my_text)
        my_button = qtw.QPushButton("Press Me!", 
        clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        self.show()
        def press_it():
            my_label.setText(f"You typed {my_text.toPlainText()}!")
            #We can return toPlainText, which return plainText
            my_text.setPlainText("You Pressed the Button")
            #setPlainText() method can set a plain text in the box
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()