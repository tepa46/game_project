from PyQt5.QtWidgets import QWidget, QDialog, QLabel
from PyQt5.QtWidgets import QPushButton, QApplication
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtCore import QSize
import game_info

SCREEN_SIZE = [500, 600]


class History_window(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initUI()

    def initUI(self):

        self.setWindowTitle('История')
        self.setGeometry(150, 150, *SCREEN_SIZE)

        self.label = QLabel(self)
        self.label.resize(500, 550)
        self.label.setText(game_info.get_history())
        self.label.setFont(QFont("Times", 16, QFont.Bold))

        self.btn = QPushButton('ЗАКРЫТЬ', self)
        self.btn.resize(500, 50)
        self.btn.move(0, 550)
        self.btn.clicked.connect(self.close_wind)

    def close_wind(self):
        self.close()
