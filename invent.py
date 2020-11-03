import sys
from PyQt5.QtWidgets import QInputDialog, QDialog
from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QListWidget
from PyQt5.QtWidgets import QLabel, QPushButton, QApplication
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import time

INVENT_SCREEN_SIZE = [300, 300]


class Invent(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Challenge')
        self.setGeometry(300, 300, *INVENT_SCREEN_SIZE)

        self.list_wid = QListWidget(self)
        self.list_wid.resize(300, 250)
        with open('inventory.txt', 'r') as input_file:
            all_file = input_file.read().split('\n')
        for line in all_file:
            self.list_wid.addItem(line)
        self.btn = QPushButton('Закрыть', self)
        self.btn.move(0, 250)
        self.btn.resize(300, 50)
        self.btn.clicked.connect(self.close_wind)

    def close_wind(self):
        self.close()
