# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 568)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputlabel = QtWidgets.QLabel(self.centralwidget)
        self.outputlabel.setGeometry(QtCore.QRect(20, 20, 351, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputlabel.setFont(font)
        self.outputlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputlabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputlabel.setObjectName("outputlabel")
        self.percentbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("%"))
        self.percentbutton.setGeometry(QtCore.QRect(40, 130, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentbutton.setFont(font)
        self.percentbutton.setObjectName("percentbutton")
        self.cbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("C"))
        self.cbutton.setGeometry(QtCore.QRect(120, 130, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cbutton.setFont(font)
        self.cbutton.setObjectName("cbutton")
        self.arrowbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.remove_it())
        self.arrowbutton.setGeometry(QtCore.QRect(210, 130, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowbutton.setFont(font)
        self.arrowbutton.setObjectName("arrowbutton")
        self.dividebutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("/"))
        self.dividebutton.setGeometry(QtCore.QRect(290, 130, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.dividebutton.setFont(font)
        self.dividebutton.setObjectName("dividebutton")
        self.ninebutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("9"))
        self.ninebutton.setGeometry(QtCore.QRect(210, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.ninebutton.setFont(font)
        self.ninebutton.setObjectName("ninebutton")
        self.eightbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("8"))
        self.eightbutton.setGeometry(QtCore.QRect(120, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightbutton.setFont(font)
        self.eightbutton.setObjectName("eightbutton")
        self.sevenbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("7"))
        self.sevenbutton.setGeometry(QtCore.QRect(40, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenbutton.setFont(font)
        self.sevenbutton.setObjectName("sevenbutton")
        self.multiplybutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("*"))
        self.multiplybutton.setGeometry(QtCore.QRect(290, 210, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplybutton.setFont(font)
        self.multiplybutton.setObjectName("multiplybutton")
        self.sixbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("6"))
        self.sixbutton.setGeometry(QtCore.QRect(210, 290, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixbutton.setFont(font)
        self.sixbutton.setObjectName("sixbutton")
        self.fivebutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("5"))
        self.fivebutton.setGeometry(QtCore.QRect(120, 290, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fivebutton.setFont(font)
        self.fivebutton.setObjectName("fivebutton")
        self.fourbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("4"))
        self.fourbutton.setGeometry(QtCore.QRect(40, 290, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourbutton.setFont(font)
        self.fourbutton.setObjectName("fourbutton")
        self.minusbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("-"))
        self.minusbutton.setGeometry(QtCore.QRect(290, 290, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusbutton.setFont(font)
        self.minusbutton.setObjectName("minusbutton")
        self.threebutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("3"))
        self.threebutton.setGeometry(QtCore.QRect(210, 370, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threebutton.setFont(font)
        self.threebutton.setObjectName("threebutton")
        self.twobutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("2"))
        self.twobutton.setGeometry(QtCore.QRect(120, 370, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twobutton.setFont(font)
        self.twobutton.setObjectName("twobutton")
        self.onebutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("1"))
        self.onebutton.setGeometry(QtCore.QRect(40, 370, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.onebutton.setFont(font)
        self.onebutton.setObjectName("onebutton")
        self.plusbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("+"))
        self.plusbutton.setGeometry(QtCore.QRect(290, 370, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusbutton.setFont(font)
        self.plusbutton.setObjectName("plusbutton")
        self.decimalbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.dot_it())
        self.decimalbutton.setGeometry(QtCore.QRect(210, 450, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalbutton.setFont(font)
        self.decimalbutton.setObjectName("decimalbutton")
        self.zerobutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.press_it("0"))
        self.zerobutton.setGeometry(QtCore.QRect(120, 450, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zerobutton.setFont(font)
        self.zerobutton.setObjectName("zerobutton")
        self.plusminusbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.plus_minus_it())
        self.plusminusbutton.setGeometry(QtCore.QRect(40, 450, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusminusbutton.setFont(font)
        self.plusminusbutton.setObjectName("plusminusbutton")
        self.equalbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.math_it())
        self.equalbutton.setGeometry(QtCore.QRect(290, 450, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalbutton.setFont(font)
        self.equalbutton.setObjectName("equalbutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    #Let's Do some math
    def math_it(self):
        screen = self.outputlabel.text()
        try:
            #Evaluate expression eval return number type
            answer = eval(screen)
            self.outputlabel.setText(str(answer))
        except:
            #Put error
            self.outputlabel.setText("ERROR")
    
    #Cahnge from positive to negative and vice-versa
    def plus_minus_it(self):
        #Grab what's on the screen already
        screen = self.outputlabel.text()
        if "-" in screen:
            self.outputlabel.setText(screen.replace("-",""))
        else:
            self.outputlabel.setText(f"-{screen}")
    
    #Remove character
    def remove_it(self):
        #Grab what's on the screen already
        screen = self.outputlabel.text()
        #Remove last item in the screen/string--list
        screen = screen[:-1]
        #Output back to the screen
        self.outputlabel.setText(screen)
        
    #Add a decimal
    def dot_it(self):
        #we want one dot only
        screen = self.outputlabel.text()
        if screen[-1] == ".":
            pass #if we have already dot we want to pass, since we need only one dot
        else:
            self.outputlabel.setText(f"{screen}.")
    
    def press_it(self,pressed):
        #Creating functionality of button press
        if pressed=="C":
            self.outputlabel.setText("0")
        else:
            #Check to see if starts with 0 and delete 0
            if self.outputlabel.text() == "0":
                self.outputlabel.setText("")
            #Concatenate the pressed  button  with what was there already
            self.outputlabel.setText(f"{self.outputlabel.text()}{pressed}") #we want put pressed along eith what there was previously, which is inside self.outputlabel.text()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputlabel.setText(_translate("MainWindow", "0"))
        self.percentbutton.setText(_translate("MainWindow", "%"))
        self.cbutton.setText(_translate("MainWindow", "C"))
        self.arrowbutton.setText(_translate("MainWindow", "<<"))
        self.dividebutton.setText(_translate("MainWindow", "/"))
        self.ninebutton.setText(_translate("MainWindow", "9"))
        self.eightbutton.setText(_translate("MainWindow", "8"))
        self.sevenbutton.setText(_translate("MainWindow", "7"))
        self.multiplybutton.setText(_translate("MainWindow", "x"))
        self.sixbutton.setText(_translate("MainWindow", "6"))
        self.fivebutton.setText(_translate("MainWindow", "5"))
        self.fourbutton.setText(_translate("MainWindow", "4"))
        self.minusbutton.setText(_translate("MainWindow", "-"))
        self.threebutton.setText(_translate("MainWindow", "3"))
        self.twobutton.setText(_translate("MainWindow", "2"))
        self.onebutton.setText(_translate("MainWindow", "1"))
        self.plusbutton.setText(_translate("MainWindow", "+"))
        self.decimalbutton.setText(_translate("MainWindow", "."))
        self.zerobutton.setText(_translate("MainWindow", "0"))
        self.plusminusbutton.setText(_translate("MainWindow", "+/-"))
        self.equalbutton.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

