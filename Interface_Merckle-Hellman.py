from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow, QFileDialog

from gui_merkel import *  # import du fichier gui.py généré par pyuic5
from merckle_hellman import *

def list_str_to_list(cle):
    cle = cle[1:len(cle) - 1].split(',')
    return [int(c) for c in cle]

def list_clepr_str_to_list(cle):
    cle = cle[1:len(cle) - 1].split(',')
    long = len(cle)
    N = int(cle[0])
    A = int(cle[1])
    cle[2] = cle[2][2:]
    cle[long - 1] = cle[long - 1][:len(cle[long - 1]) - 1]
    liste = []
    for i in range(long - 2):
        liste.append(int(cle[i + 2]))
    return [N, A, liste]

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ## Définition des actions du menu
        self.ui.actionCr_er_une_paire_de_clefs.triggered.connect(self.creer_paire_cle)
        self.ui.actionCoder_un_message.triggered.connect(self.coder_message)
        self.ui.actionD_coder_un_message.triggered.connect(self.decoder_message)

    def creer_paire_cle(self):
        cle_pr = cle_privee()
        self.ui.lineEdit.setText(str(cle_pr))
        self.ui.lineEdit_2.setText(str(cle_publique(cle_pr)))
        
    def coder_message(self):
        cle = self.ui.lineEdit_2.text()
        if cle:
            cle = list_str_to_list(cle)
            if len(cle)!=8:
                print("La clé publique n'est pas du bon format")
            else:
                self.ui.textEdit_2.setText(str(codage(cle, self.ui.textEdit.toPlainText())))
        else:
            print("Il faut une clé publique pour coder")

    def decoder_message(self):
        cle = self.ui.lineEdit.text()
        if cle:
            cle = list_clepr_str_to_list(cle)
            message_code = self.ui.textEdit_2.toPlainText()
            if message_code:
                message_code = list_str_to_list(message_code)
                self.ui.textEdit.setText(str(decodage(message_code, cle)))
        else:
            print("Il faut une clé privée pour décoder")


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
