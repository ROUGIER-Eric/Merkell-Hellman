#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow, QFileDialog

import gui  # import du fichier gui.py généré par pyuic5

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)

        # Définition des actions http://pyqt.sourceforge.net/Docs/PyQt4/
        self.ui.actionOuvrir_un_fichier.triggered.connect(self.action_ouvrirFichier)
        self.ui.actionEnregistrer_sous.triggered.connect(self.action_enregistrerFichier)
        self.ui.pushButton.clicked.connect(self.code)
        self.ui.actionQuitter.triggered.connect(self.close)

    def action_ouvrirFichier(self):
        # Création d'une fenêtre de dialogue
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
	   # Exécute l'ouverture de cette fenêtre pour récupérer l'arborescence du fichier
        filename = dialog.getOpenFileName(None, "Ouvrir un document", "../","Mes fichiers (*.txt)")
	   #selectedFiles()
        fichier = open(filename[0], "r")
        texte = fichier.read()
        self.ui.textEdit_fichier_source.setText(texte)
        self.ui.textEdit_fichier_destination.setText("")
        self.ui.lineEdit_nombre_lettres_source.setText("")
        self.ui.lineEdit_nombre_lettres_destination.setText("")
        fichier.close()

    def action_enregistrerFichier(self):
        # Création d'une fenêtre de dialogue
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
	   # Exécute la fenêtre de dialogue en écriture pour récupérer l'arborescence
        filename = dialog.getSaveFileName(None,"Enregistrer fichier", "sauve.txt", "Mes Fichiers (*.txt)")
        fichier = open(filename[0], "w")
        fichier.write(self.ui.textEdit_fichier_destination.toPlainText())
        fichier.close()



    def rotation(self, chaine, x):
        """
         Effectue une rotation de x caractères vers la droite:
         >>> rotation('abcde', 2)
         'cdeab'
        """
        return chaine[x:] + chaine[:x]

    def index(self, c, chaine):
        """
         Trouve l'index de c dans la chaine:
         >>> index('n', 'bonjour')
         2
        """
        for i in range(len(chaine)):
            if (c == chaine[i]):
                return i
        return -1

    def chiffre(self):
        """
         Chiffre une chaîne quelconque
         >>> chiffre('Bonjour les amis!', 3)
         'Erqmrxu ohv dplv!'
        """
        minuscules = 'abcdefghijklmnopqrstuvwxyz'
        majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        texte_source = self.ui.textEdit_fichier_source.toPlainText()
        x = int(self.ui.lineEdit_nombre_decalage.text())
        r_min = self.rotation(minuscules, x)
        r_maj = self.rotation(majuscules, x)
        resultat = ''
        for lettre in texte_source:
            if lettre in minuscules:
                resultat = resultat + r_min[self.index(lettre, minuscules)]
            elif lettre in majuscules:
                resultat = resultat + r_maj[self.index(lettre, majuscules)]
            else:
                resultat = resultat + lettre
        self.ui.textEdit_fichier_destination.setText(resultat)

    def comptage_lettres(self):
        minuscules = 'abcdefghijklmnopqrstuvwxyz'
        texte_source = self.ui.textEdit_fichier_source.toPlainText()
        nombre_lettres = " | "
        for lettre in minuscules:
            n = 0
            for car in texte_source:
                if car == lettre:
                    n +=1
            nombre_lettres += str(n) + " | "
        self.ui.lineEdit_nombre_lettres_source.setText(nombre_lettres)

        texte_destination = self.ui.textEdit_fichier_destination.toPlainText()
        nombre_lettres = " | "
        for lettre in minuscules:
            n = 0
            for car in texte_destination:
                if car == lettre:
                    n +=1
            nombre_lettres += str(n) + " | "
        self.ui.lineEdit_nombre_lettres_destination.setText(nombre_lettres)

    def code(self):
        self.chiffre()
        self.comptage_lettres()

    def closeEvent(self, event):
        close = QMessageBox()
        close.setText("Sûr ?")
        close.setStandardButtons(QMessageBox.Close | QMessageBox.Cancel)
        close = close.exec()
        if close == QMessageBox.Close:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
