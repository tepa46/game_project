from PyQt5.QtWidgets import QWidget, QDialog, QInputDialog, QLabel
from PyQt5.QtWidgets import QPushButton, QApplication
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import os

SCREEN_SIZE = [1000, 1000]


class AddCustomLevel(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.x = 0
        self.y = 0

    def initUI(self):
        self.setWindowTitle('Выбор места кнопки')
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setFixedSize(*SCREEN_SIZE)

        self.btn_close = QPushButton('Выбрать', self)
        self.btn_close.resize(50, 50)
        self.btn_close.move(950, 950)
        self.btn_close.clicked.connect(self.exit)

        with open('new_levels_info/level.txt', 'r') as input_file:
            level = input_file.readline()
        with open('new_levels_info/file.txt', 'r') as input_file:
            file = input_file.readline()
        oImage = QImage(f'{level}/{file}/background.png')
        sImage = oImage.scaled(QSize(*SCREEN_SIZE))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def mousePressEvent(self, event):
        if event.x() < 950 or event.y() < 950:
            self.x = event.x()
            self.y = event.y()
            with open('new_levels_info/coords.txt', 'w') as output_file:
                output_file.write(str(event.x()) + ' ' + str(event.y()))

    def exit(self):
        self.close()
