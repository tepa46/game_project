import sys
from PyQt5.QtWidgets import QInputDialog, QPushButton, QApplication, QMainWindow
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import add_custom_level
import os
import shutil

SCREEN_SIZE = [1000, 1000]


class EditorMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Редактор уровней')
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setFixedSize(*SCREEN_SIZE)

        oImage = QImage('main_menu_background')
        sImage = oImage.scaled(QSize(*SCREEN_SIZE))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.btn_start = QPushButton('СОЗДАТЬ', self)
        self.btn_start.move(400, 500)
        self.btn_start.resize(200, 100)
        self.btn_start.clicked.connect(self.make)

        self.btn_delete = QPushButton('УДАЛИТЬ', self)
        self.btn_delete.move(400, 630)
        self.btn_delete.resize(200, 100)
        self.btn_delete.clicked.connect(self.delete_level)

        self.btn_exit = QPushButton('ВЫЙТИ', self)
        self.btn_exit.move(400, 760)
        self.btn_exit.resize(200, 100)
        self.btn_exit.clicked.connect(self.exit)

        self.show()

    def make(self):
        self.close()
        self.editor = add_custom_level.AddCustomLevel()
        self.editor.show()

    def delete_level(self):
        with open('unlock_levels.txt', 'r', encoding='utf8') as input_file:
            levels_lst = input_file.read().split('\n')
        level_name, ok_pressed = QInputDialog.getItem(
            self, "Выбор уровня", "Выберите уровень для удаления",
            levels_lst, 0, True)
        if ok_pressed:
            if level_name != 'level_1' and level_name != 'level_2' and level_name != 'level_3':
                shutil.rmtree(level_name)
                output_file = open('unlock_levels.txt', 'w', encoding='utf8')
                output_file.close()
                first = True
                with open('unlock_levels.txt', 'a', encoding='utf8') as output_file:
                    for lvl in levels_lst:
                        if lvl != level_name:
                            if first:
                                output_file.write(lvl)
                                first = False
                            else:
                                output_file.write('\n' + lvl)

    def exit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pril = EditorMenu()
    sys.exit(app.exec())
