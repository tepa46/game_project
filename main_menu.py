import sys
import os
from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QInputDialog, QDialog
from PyQt5.QtWidgets import QLabel, QPushButton, QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush, QColor
from PyQt5.QtCore import QSize
import main_file
import game_info

SCREEN_SIZE = [1000, 1000]


class Main_menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Undertale')
        self.setGeometry(0, 0, *SCREEN_SIZE)

        oImage = QImage('main_menu_background')
        sImage = oImage.scaled(QSize(*SCREEN_SIZE))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.btn_play = QPushButton('ИГРАТЬ', self)
        self.btn_play.move(400, 500)
        self.btn_play.resize(200, 100)
        self.btn_play.clicked.connect(self.play)

        self.btn_exit = QPushButton('ВЫЙТИ', self)
        self.btn_exit.move(400, 630)
        self.btn_exit.resize(200, 100)
        self.btn_exit.clicked.connect(self.exit)

        self.show()

    def play(self):
        level, ok_pressed = QInputDialog.getItem(
            self, "Выберите уровень", "уровни",
            ("1", "2", "3"), 1, False)
        if ok_pressed:
            self.close()
            game_info.put_level(level)
            game_info.put_file('room_1')
            game_info.clear_files()
            self.ex = main_file.Window()
            self.ex.show()
        else:
            exit()

    def exit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pril = Main_menu()
    sys.exit(app.exec())
