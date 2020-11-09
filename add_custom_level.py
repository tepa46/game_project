from PyQt5.QtWidgets import QWidget, QDialog, QInputDialog, QFileDialog
from PyQt5.QtWidgets import QPushButton, QApplication
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import os
import shutil
import blank_displaying

SCREEN_SIZE = [1000, 1000]


class AddCustomLevel(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cnt = 0
        self.level = ''

    def initUI(self):
        self.setWindowTitle('Редактор уровней')
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setFixedSize(*SCREEN_SIZE)

        oImage = QImage('main_menu_background')
        sImage = oImage.scaled(QSize(*SCREEN_SIZE))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.btn_make_room = QPushButton('СОЗДАТЬ КОМНАТУ', self)
        self.btn_make_room.move(400, 500)
        self.btn_make_room.resize(200, 100)
        self.btn_make_room.clicked.connect(self.make_room)

        self.btn_delete_room = QPushButton('УДАЛИТЬ КОМНАТУ', self)
        self.btn_delete_room.move(400, 630)
        self.btn_delete_room.resize(200, 100)
        self.btn_delete_room.clicked.connect(self.delete_room)

        self.btn_exit = QPushButton('ЗАКРЫТЬ', self)
        self.btn_exit.move(400, 760)
        self.btn_exit.resize(200, 100)
        self.btn_exit.clicked.connect(self.exit)

        self.make_directory()

    def make_directory(self):
        path, ok_pressed = QInputDialog.getText(self, "Введите название",
                                                "Как будет называться уровень?")
        if ok_pressed:
            os.mkdir(path)
            with open('new_levels_info/level.txt', 'w') as output_file:
                output_file.write(path)

    def make_room(self):
        self.cnt += 1
        path = f'room_{self.cnt}'
        with open('new_levels_info/level.txt', 'r') as input_file:
            level = input_file.readline()
        os.mkdir(os.path.join(level, path))
        with open('new_levels_info/file.txt', 'w') as output_file:
            output_file.write(path)
        self.choose_background(os.path.join(level, path))
        self.config_buttons(os.path.join(level, path))

    def choose_background(self, path):
        fname = QFileDialog.getOpenFileName(self, 'Выберите фон комнаты', '')[0]
        shutil.copy(fname, f'{path}/background.png')

    def make_button(self, path, num):
        self.blank = blank_displaying.AddCustomLevel()
        self.blank.show()
        with open('new_levels_info/coords.txt', 'r') as input_file:
            coords = input_file.readline().split(' ')
        with open(f'{path}/button_{num}.txt', 'w') as output_file:
            output_file.write(coords[0] + ' ' + coords[1] + '\n')

        self.button_sizes(path, num)
        self.button_command(path, num)
        self.button_way(path, num)

    def button_way(self, path, num):
        way, ok_pressed = QInputDialog.getText(self, "Введите строку",
                                               "В какую комнату будет вести кнопка(или в эту же)?")
        if ok_pressed:
            with open(f'{path}/button_{num}.txt', 'a') as output_file:
                output_file.write(way + '\n')

    def button_command(self, path, num):
        command, ok_pressed = QInputDialog.getItem(
            self, "Выбор команды", "Выберите команду",
            ('ПОСМОТРЕТЬ', 'ВОЙТИ В КОМНАТУ', 'ОБРАТНО', 'ПРОЙТИ ДОЛЬШЕ'), 0, True)
        if ok_pressed:
            with open(f'{path}/button_{num}.txt', 'a') as output_file:
                output_file.write(command + '\n')

    def button_sizes(self, path, num):
        btn_size_x, ok_pressed = QInputDialog.getText(self, "Введите значение",
                                                      "Какой размер кнопки (по длине)?")

        if ok_pressed:
            with open(f'{path}/button_{num}.txt', 'a') as output_file:
                output_file.write(btn_size_x + ' ')

        btn_size_y, ok_pressed = QInputDialog.getText(self, "Введите значение",
                                                      "Какой размер кнопки (по ширине)?")

        if ok_pressed:
            with open(f'{path}/button_{num}.txt', 'a') as output_file:
                output_file.write(btn_size_y + '\n')

    def config_buttons(self, path):
        for num in range(1, 6):
            input_file = open(f'{path}/button_{num}.txt', 'w')
            input_file.write('0 0\n0 0\n\n\n\n')
            input_file.close()
        btn_cnt, ok_pressed = QInputDialog.getText(self, "Введите значение",
                                                   "Сколько кнопок вы хотите?")
        if ok_pressed:
            for num in range(1, int(btn_cnt) + 1):
                self.make_button(path, num)

    def delete_room(self):
        path, ok_pressed = QInputDialog.getText(self, "Введите название",
                                                "Какую комнату удалить?")
        if ok_pressed:
            os.remove(path)

    def exit(self):
        self.close()
