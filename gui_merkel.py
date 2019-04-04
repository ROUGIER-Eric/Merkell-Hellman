# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_merkel.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("mainwindows")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 19, 531, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 101, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 49, 531, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 80, 531, 201))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 290, 531, 251))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 91, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 390, 91, 20))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        self.menuCr_er_une_paire_de_clefs = QtWidgets.QMenu(self.menubar)
        self.menuCr_er_une_paire_de_clefs.setObjectName("menuCr_er_une_paire_de_clefs")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCr_er_une_paire_de_clefs = QtWidgets.QAction(MainWindow)
        self.actionCr_er_une_paire_de_clefs.setObjectName("actionCr_er_une_paire_de_clefs")
        self.actionCoder_un_message = QtWidgets.QAction(MainWindow)
        self.actionCoder_un_message.setObjectName("actionCoder_un_message")
        self.actionD_coder_un_message = QtWidgets.QAction(MainWindow)
        self.actionD_coder_un_message.setObjectName("actionD_coder_un_message")
        self.menuCr_er_une_paire_de_clefs.addAction(self.actionCr_er_une_paire_de_clefs)
        self.menuCr_er_une_paire_de_clefs.addAction(self.actionCoder_un_message)
        self.menuCr_er_une_paire_de_clefs.addAction(self.actionD_coder_un_message)
        self.menubar.addAction(self.menuCr_er_une_paire_de_clefs.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Algorithme de Merckle - Hellmann"))
        self.label.setText(_translate("MainWindow", "Clef Privée"))
        self.label_2.setText(_translate("MainWindow", "Texte à coder"))
        self.label_3.setText(_translate("MainWindow", "Clef Publique"))
        self.label_4.setText(_translate("MainWindow", "Texte crypté"))
        self.menuCr_er_une_paire_de_clefs.setTitle(_translate("MainWindow", "Menu"))
        self.actionCr_er_une_paire_de_clefs.setText(_translate("MainWindow", "Créer une paire de clefs"))
        self.actionCoder_un_message.setText(_translate("MainWindow", "Coder un message"))
        self.actionD_coder_un_message.setText(_translate("MainWindow", "Décoder un message"))

