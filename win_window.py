import sys
import os
from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QInputDialog, QDialog
from PyQt5.QtWidgets import QLabel, QPushButton, QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush, QColor
from PyQt5.QtCore import QSize, Qt
import main_menu

SCREEN_SIZE = [1000, 1000]


class Win_window(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initUI()

    def initUI(self):
            self.setWindowTitle('ПОБЕДА')
            self.setGeometry(0, 0, *SCREEN_SIZE)

            oImage = QImage('win/win.png')
            sImage = oImage.scaled(QSize(*SCREEN_SIZE))
            palette = QPalette()
            palette.setBrush(QPalette.Window, QBrush(sImage))
            self.setPalette(palette)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.close()
            self.main_menu = main_menu.Main_menu()
            self.main_menu.show()
