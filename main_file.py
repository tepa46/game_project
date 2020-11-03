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

SCREEN_SIZE = [1000, 1000]

file = 'room_1'


class Window(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initUI()

    def initUI(self):
        os.system(r'nul>inventory.txt')
        os.system(r'nul>completed_tasks.txt')

        self.setWindowTitle('Undertale')
        self.setGeometry(0, 0, *SCREEN_SIZE)

        self.button_1 = QPushButton(self)
        self.button_1.clicked.connect(lambda: self.pushed_button('/button_1.txt'))

        self.button_2 = QPushButton(self)
        self.button_2.clicked.connect(lambda: self.pushed_button('/button_2.txt'))

        self.button_3 = QPushButton(self)
        self.button_3.clicked.connect(lambda: self.pushed_button('/button_3.txt'))

        self.button_4 = QPushButton(self)
        self.button_4.clicked.connect(lambda: self.pushed_button('/button_4.txt'))

        self.button_5 = QPushButton(self)
        self.button_5.clicked.connect(lambda: self.pushed_button('/button_5.txt'))

        self.button_invent = QPushButton('ИНВЕНТАРЬ', self)
        self.button_invent.clicked.connect(self.invent_show)

        self.start_game()
        self.make_room(f'{file}/background.png')

    def make_room(self, text):
        self.make_background(text)
        self.make_buttons()

    def make_buttons(self):
        button_config.button_config(self, file)
        self.show()

    def make_background(self, file_name):
        oImage = QImage(file_name)
        sImage = oImage.scaled(QSize(*SCREEN_SIZE))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def pushed_button(self, button_name):
        global file
        with open(file + button_name, 'r', encoding='utf8') as input_file:
            text = input_file.read()
            command = text.split('\n')[2]
            new_file = text.split('\n')[3]

        code = button_treatment.button_treatment(self, command, new_file + button_name, new_file)
        if code == 1:
            self.update()
            file = new_file
            self.make_room(f'{file}/background.png')
            QApplication.processEvents()
        if code == 2:
            self.update()
            file = new_file
            self.make_room('win/win.png')
            self.start_game()
            QApplication.processEvents()
        if code == 3:
            self.update()
            file = new_file
            self.make_room('lost/lost.png')
            self.start_game()
            QApplication.processEvents()

    def invent_show(self):
        self.invent_view = invent.Invent()
        self.invent_view.show()

    def start_game(self):
        level, ok_pressed = QInputDialog.getItem(
            self, "Выберите уровень", "уровни",
            ("1", "2", "3"), 1, False)
        if ok_pressed:
            global file
            file = 'room_1'
            os.system(r'nul>completed_tasks.txt')
            os.system(r'nul>inventory.txt')
            self.make_room(f'{file}/background.png')
        else:
            exit()
