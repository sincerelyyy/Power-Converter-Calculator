# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 13:04:56 2021

@author: cory.li
"""

import sys
from ui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtGui import QPixmap


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui._button_confirm.clicked.connect(self.calculate)
        
        self.ui._RadioButtonType1.toggled.connect(self.onClicked)
        self.ui._RadioButtonType2.toggled.connect(self.onClicked)
        self.ui._RadioButtonType3.toggled.connect(self.onClicked)

        self.ui._RadioButtonA.toggled.connect(self.onClicked)
        self.ui._RadioButtonB.toggled.connect(self.onClicked)
        
        


    def calculate(self):
        msgBox = QMessageBox()
            
        msgBox.setInformativeText("formativeText")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec_()        #ret, if ret == QMessageBox.Save: if ret == QMessageBox.Discard

    
    def onClicked(self):
        _type = 0

        if self.ui._RadioButtonType1.isChecked() == True:       # type 1
            _type = 1
            #self.ui._editA_CrossoverFreq.setEnabled(self.ui._RadioButtonA.isChecked())

        if self.ui._RadioButtonType2.isChecked() == True:       # type 2
            _type = 2
            
            #self.ui._editA_CrossoverFreq.setEnabled(not self.ui._RadioButtonA.isChecked())


        if self.ui._RadioButtonType3.isChecked() == True:       # type 3
            _type = 3
            

        if _type == 1:
            if self.ui._RadioButtonA.isChecked() == True:
                _AorB()
                print("type = 1 , radio A")

        if _type == 2:
            if self.ui._RadioButtonB.isChecked() == True:
                _AorB()
                print("type = 2 , radio B")


    def _AorB (self):
        
        if self.ui._RadioButtonA.ischecked() == True:
            print("A")
        if self.ui._RadioButtonB.isChecked() == True:
            print("B")




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())