from PyQt5.QtWidgets import QWidget, QDialog, QInputDialog
from PyQt5.QtWidgets import QPushButton
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
        self.setGeometry(1000, 50, *SCREEN_SIZE)
        self.setFixedSize(*SCREEN_SIZE)

        self.btn_close = QPushButton('Выбрать', self)
        self.btn_close.resize(50, 50)
        self.btn_close.move(950, 950)
        self.btn_close.clicked.connect(self.exit)

        with open('new_levels_info/level.txt', 'r', encoding='utf8') as input_file:
            level = input_file.readline()
        with open('new_levels_info/file.txt', 'r', encoding='utf8') as input_file:
            file = input_file.readline()
        oImage = QImage(f'{level}/{file}/background.png')
        sImage = oImage.scaled(QSize(*SCREEN_SIZE))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.show()

    def mousePressEvent(self, event):
        if event.x() < 950 or event.y() < 950:
            self.x = event.x()
            self.y = event.y()
            with open('new_levels_info/coords.txt', 'w') as output_file:
                output_file.write(str(event.x()) + ' ' + str(event.y()))

    def exit(self):
        with open('new_levels_info/coords.txt', 'r', encoding='utf8') as input_file:
            coords = input_file.readline().split(' ')
        with open('new_levels_info/level.txt', 'r', encoding='utf8') as input_file:
            level = input_file.readline()
        with open('new_levels_info/file.txt', 'r', encoding='utf8') as input_file:
            file = input_file.readline()
        path = os.path.join(level, file)
        with open('new_levels_info/num.txt', 'r', encoding='utf8') as input_file:
            num = input_file.readline()
        with open(f'{path}/button_{num}.txt', 'w', encoding='utf8') as output_file:
            output_file.write(coords[0] + ' ' + coords[1] + '\n')
        self.button_sizes(path, num)
        self.button_command(path, num)
        self.close()

    def button_way(self, path, num):
        way, ok_pressed = QInputDialog.getText(self, "Введите строку",
                                               "В какую комнату будет вести кнопка(или в эту же)?")
        if ok_pressed:
            with open(f'{path}/button_{num}.txt', 'a', encoding='utf8') as output_file:
                output_file.write(way + '\n')

    def button_command(self, path, num):
        command_lst = ['ПОСМОТРЕТЬ', 'ВОЙТИ В КОМНАТУ', 'ОБРАТНО', 'ПРОЙТИ ДАЛЬШЕ', 'ПРЕДОСТАВИТЬ ПАРОЛЬ']
        command, ok_pressed = QInputDialog.getItem(
            self, "Выбор команды", "Выберите команду",
            command_lst, 0, True)
        if ok_pressed:
            ind = command_lst.index(command)
            with open(f'{path}/button_{num}.txt', 'a', encoding='utf8') as output_file:
                output_file.write(command_lst[ind] + '\n')

            self.button_way(path, num)

            if command_lst[ind] == 'ПОСМОТРЕТЬ':
                self.new_chall(path, num)

    def new_chall(self, path, num):
        with open('new_levels_info/chall_num.txt', 'r', encoding='utf8') as input_file:
            chall_num = input_file.readline()
        with open(f'{path}/button_{num}.txt', 'a', encoding='utf8') as output_file:
            output_file.write(chall_num + '\n')
        with open('new_levels_info/chall_num.txt', 'w', encoding='utf8') as output_file:
            output_file.write(str(int(chall_num) + 1))

    def button_sizes(self, path, num):
        btn_size_x, ok_pressed = QInputDialog.getText(self, "Введите значение",
                                                      "Какой размер кнопки (по длине)?")

        if ok_pressed:
            with open(f'{path}/button_{num}.txt', 'a', encoding='utf8') as output_file:
                output_file.write(btn_size_x + ' ')

        btn_size_y, ok_pressed = QInputDialog.getText(self, "Введите значение",
                                                      "Какой размер кнопки (по ширине)?")

        if ok_pressed:
            with open(f'{path}/button_{num}.txt', 'a', encoding='utf8') as output_file:
                output_file.write(btn_size_y + '\n')
