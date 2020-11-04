import sys
import os
from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QInputDialog, QDialog
from PyQt5.QtWidgets import QLabel, QPushButton, QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush, QColor
from PyQt5.QtCore import QSize
import button_config
import button_treatment
import time
import invent
import win_window

SCREEN_SIZE = [1000, 1000]

file = 'room_1'


class Window(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initUI()

    def initUI(self):

        with open('level_num.txt', 'r', encoding='utf8') as input_file:
            level = input_file.readline()
        with open(f'{level}/file.txt', 'r', encoding='utf8') as input_file:
            file = input_file.readline()

        os.system(fr'nul>{level}/inventory.txt')
        os.system(fr'nul>{level}/completed_tasks.txt')

        self.setWindowTitle('Undertale')
        self.setGeometry(0, 0, *SCREEN_SIZE)

        self.button_1 = QPushButton(self)
        self.button_1.clicked.connect(lambda: self.pushed_button('button_1.txt'))

        self.button_2 = QPushButton(self)
        self.button_2.clicked.connect(lambda: self.pushed_button('button_2.txt'))

        self.button_3 = QPushButton(self)
        self.button_3.clicked.connect(lambda: self.pushed_button('button_3.txt'))

        self.button_4 = QPushButton(self)
        self.button_4.clicked.connect(lambda: self.pushed_button('button_4.txt'))

        self.button_5 = QPushButton(self)
        self.button_5.clicked.connect(lambda: self.pushed_button('button_5.txt'))

        self.button_invent = QPushButton('ИНВЕНТАРЬ', self)
        self.button_invent.clicked.connect(self.invent_show)

        self.make_room(f'{level}/{file}/background.png')

    def make_room(self, text):
        self.make_background(text)
        self.make_buttons()

    def make_buttons(self):
        button_config.button_config(self)
        self.show()

    def make_background(self, file_name):
        oImage = QImage(file_name)
        sImage = oImage.scaled(QSize(*SCREEN_SIZE))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def pushed_button(self, button_name):
        with open('level_num.txt', 'r', encoding='utf8') as input_file:
            level = input_file.readline()
        with open(f'{level}/file.txt', 'r', encoding='utf8') as input_file:
            file = input_file.readline()
        with open(f'{level}/{file}/{button_name}', 'r', encoding='utf8') as input_file:
            text = input_file.read()
            command = text.split('\n')[2]
            new_file = text.split('\n')[3]

        code = button_treatment.button_treatment(self, command, button_name)
        if code == 1:
            self.update()
            os.system(fr'nul>{level}/file.txt')
            with open(f'{level}/file.txt', 'a', encoding='utf8') as output_file:
                output_file.write(new_file)
            with open('level_num.txt', 'r', encoding='utf8') as input_file:
                level = input_file.readline()
            with open(f'{level}/file.txt', 'r', encoding='utf8') as input_file:
                file = input_file.readline()
            self.make_room(f'{level}/{file}/background.png')
            QApplication.processEvents()
        if code == 2:
            os.system(fr'nul>{level}/file.txt')
            with open(f'{level}/file.txt', 'a', encoding='utf8') as output_file:
                output_file.write(new_file)
            self.close()
            self.win_window = win_window.Win_window()
            self.win_window.show()
        if code == 3:
            os.system(fr'nul>{level}/file.txt')
            with open(f'{level}/file.txt', 'a', encoding='utf8') as output_file:
                output_file.write(new_file)
            # self.make_room('lost/lost.png')
            self.close()

    def invent_show(self):
        self.invent_view = invent.Invent()
        self.invent_view.show()
