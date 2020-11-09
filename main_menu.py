import sys
from PyQt5.QtWidgets import QInputDialog, QPushButton, QApplication, QMainWindow
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import main_file
import game_info

SCREEN_SIZE = [1000, 1000]


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Undertale')
        self.setFixedSize(*SCREEN_SIZE)

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
        open('game_info.py')
        game_info.info.get_unlock_levels()
        levels = game_info.info.unlock_levels
        level, ok_pressed = QInputDialog.getItem(
            self, "Выбор уровня", "Выберите уровень или напишите его название",
            levels, 0, True)
        if ok_pressed:
            self.close()
            game_info.info.put_level(level)
            game_info.info.put_file('room_1')
            game_info.info.clear_files()
            game_info.info.init_all_info()
            self.ex = main_file.Engine()
            self.ex.show()

    def exit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pril = MainMenu()
    sys.exit(app.exec())
