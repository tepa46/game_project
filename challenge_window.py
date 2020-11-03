import sys
from PyQt5.QtWidgets import QInputDialog, QDialog
from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton, QApplication
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import time

CHALLENGE_SCREEN_SIZE = [280, 100]


class Challenge_window(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Challenge')
        self.setGeometry(300, 300, *CHALLENGE_SCREEN_SIZE)

        self.label = QLabel(self)

        with open('sequence_text.txt', 'r', encoding='utf8') as input_file:
            sequence_text = input_file.read()

        if sequence_text != 'Вы уже тут все посмотрели' and sequence_text != 'Здесь ничего нет':
            self.label.setText('Вы нашли новую часть последовательности: ' + '\n' + sequence_text)
        else:
            self.label.setText(sequence_text)
        self.label.move(20, 20)

        self.btn = QPushButton('OK', self)
        self.btn.move(100, 70)
        self.btn.clicked.connect(self.close_window)

    def close_window(self):
        with open('sequence_text.txt', 'r', encoding='utf8') as input_file:
            sequence_text = input_file.read()

        if sequence_text != 'Вы уже тут все посмотрели' and sequence_text != 'Здесь ничего нет':
            self.update()
            self.label.setText('Вы можете увидеть новый предмет' + '\n' + 'открыв инвентарь')
            QApplication.processEvents()
            time.sleep(1.4)
        self.close()
