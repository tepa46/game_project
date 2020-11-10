from PyQt5.QtWidgets import QWidget, QDialog, QInputDialog, QFileDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import os
import shutil
import blank_displaying

SCREEN_SIZE = [700, 700]


class AddCustomLevel(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cnt = 0
        self.btn_num = 0

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
        self.btn_make_room.move(400, 370)
        self.btn_make_room.resize(200, 100)
        self.btn_make_room.clicked.connect(self.make_room)

        self.btn_make_room = QPushButton('СОЗДАТЬ КНОПКУ', self)
        self.btn_make_room.move(400, 500)
        self.btn_make_room.resize(200, 100)
        self.btn_make_room.clicked.connect(self.make_button)

        self.btn_delete_room = QPushButton('ЗАВЕРШЕНИЕ СОЗДАНИЯ', self)
        self.btn_delete_room.move(400, 630)
        self.btn_delete_room.resize(200, 100)
        self.btn_delete_room.clicked.connect(self.finish_add)

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
            with open('new_levels_info/level.txt', 'w', encoding='utf8') as output_file:
                output_file.write(path)

            with open('new_levels_info/chall_num.txt', 'w', encoding='utf8') as output_file:
                output_file.write('1')

    def make_room(self):
        self.cnt += 1
        path = f'room_{self.cnt}'
        with open('new_levels_info/level.txt', 'r', encoding='utf8') as input_file:
            level = input_file.readline()
        os.mkdir(os.path.join(level, path))
        with open('new_levels_info/file.txt', 'w', encoding='utf8') as output_file:
            output_file.write(path)
        with open(f'{level}/{path}/room_history.txt', 'w', encoding='utf8') as output_file:
            output_file.write('This room has no history')
        self.choose_background(os.path.join(level, path))
        self.config_buttons(os.path.join(level, path))
        self.btn_num = 1

    def choose_background(self, path):
        fname = QFileDialog.getOpenFileName(self, 'Выберите фон комнаты', '')[0]
        shutil.copy(fname, f'{path}/background.png')

    def make_button(self):
        with open('new_levels_info/num.txt', 'w', encoding='utf8') as output_file:
            output_file.write(str(self.btn_num))
        self.blank = blank_displaying.AddCustomLevel()
        self.show()
        self.btn_num += 1

    def config_buttons(self, path):
        for num in range(1, 6):
            input_file = open(f'{path}/button_{num}.txt', 'w', encoding='utf8')
            input_file.write('0 0\n0 0\n\n\n\n')
            input_file.close()

    def finish_add(self):
        with open('new_levels_info/level.txt', 'r', encoding='utf8') as input_file:
            level = input_file.readline()
        with open('new_levels_info/chall_num.txt', 'r', encoding='utf8') as input_file:
            chall_num = input_file.readline()
        output_file = open(f'{level}/inventory.txt', 'w', encoding='utf8')
        output_file.close()

        output_file = open(f'{level}/file.txt', 'w', encoding='utf8')
        output_file.close()

        output_file = open(f'{level}/inventory.txt', 'w', encoding='utf8')
        output_file.close()

        output_file = open(f'{level}/completed_tasks.txt', 'w', encoding='utf8')
        output_file.close()

        output_file = open(f'{level}/sequence_text.txt', 'w', encoding='utf8')
        output_file.close()

        output_file = open(f'{level}/rooms_history_used.txt', 'w', encoding='utf8')
        output_file.close()

        answer_d = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

        with open(f'{level}/challenge.txt', 'a', encoding='utf8') as output_file:
            for _ in range(int(chall_num) - 1):
                text, ok_pressed = QInputDialog.getText(self, "Введите строку",
                                                        "Какую часть пароля тут найдет пользователь?")
                if ok_pressed:
                    output_file.write(text + '\n')
                    for sym in text:
                        answer_d[sym] += 1

        ans = 0
        for key in answer_d:
            ans = max(ans, answer_d[key])
        key_ans = ''
        for key in answer_d:
            if answer_d[key] == ans:
                key_ans = key

        with open(f'{level}/answer.txt', 'w', encoding='utf8') as output_file:
            output_file.write(key_ans)

        with open('unlock_levels.txt', 'a', encoding='utf8') as output_file:
            output_file.write('\n' + level)
        self.exit()

    def exit(self):
        self.close()
