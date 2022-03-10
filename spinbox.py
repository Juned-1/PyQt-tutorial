#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 10:03:44 2021
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 10:03:44 2021

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
        #Create Spin box
        #By default pyqt spin box deal with number
        my_spin = qtw.QSpinBox(self,
                    value = 10,
                    maximum = 100,
                    minimum = 0,
                    singleStep = 5,
                    prefix = "#",
                    suffix = " Order")
        #Spin box take value within certein limit, value gives by default
        #value, maximum and minimum how much maximum and minimum we want 
        #to give, singleStep define how much step should increase or decrease
        #on one step forward or backward, we can add prfix and suffix in
        #spin box
        #We can use QDoubleSpinBox(), instead of QSpinBox to spin element
        #by floating point number and set single Step ro floating value
        ''''
                my_spin = qtw.QDoubleSpinBox(self,
                    value = 10,
                    maximum = 100,
                    minimum = 0,
                    singleStep = 5.5,
                    prefix = "#",
                    suffix = " Order")
        '''
        #change font size of spin box
        my_spin.setFont(qtg.QFont('Helvetica',18))
        #Adding spin box to layout
        self.layout().addWidget(my_spin)
        my_button = qtw.QPushButton("Press Me!", 
        clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        self.show()
        def press_it():
            my_label.setText(f"You pick {my_spin.value()}!")
            #We can return value(), which return current value of in spin box

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
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
        #Create Spin box
        #By default pyqt spin box deal with number
        my_spin = qtw.QSpinBox(self,
                    value = 10,
                    maximum = 100,
                    minimum = 0,
                    singleStep = 5,
                    prefix = "#",
                    suffix = " Order")
        #Spin box take value within certein limit, value gives by default
        #value, maximum and minimum how much maximum and minimum we want 
        #to give, singleStep define how much step should increase or decrease
        #on one step forward or backward, we can add prfix and suffix in
        #spin box
        #We can use QDoubleSpinBox(), instead of QSpinBox to spin element
        #by floating point number and set single Step ro floating value
        ''''
                my_spin = qtw.QDoubleSpinBox(self,
                    value = 10,
                    maximum = 100,
                    minimum = 0,
                    singleStep = 5.5,
                    prefix = "#",
                    suffix = " Order")
        '''
        #change font size of spin box
        my_spin.setFont(qtg.QFont('Helvetica',18))
        #Adding spin box to layout
        self.layout().addWidget(my_spin)
        my_button = qtw.QPushButton("Press Me!", 
        clicked = lambda: press_it())
        self.layout().addWidget(my_button)
        self.show()
        def press_it():
            my_label.setText(f"You pick {my_spin.value()}!")
            #We can return value(), which return current value of in spin box

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()