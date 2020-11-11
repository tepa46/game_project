from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt
import main_menu
import game_info

SCREEN_SIZE = [700, 700]


class WinWindow(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ПОБЕДА')
        self.setFixedSize(*SCREEN_SIZE)

        oImage = QImage('win/win.png')
        sImage = oImage.scaled(QSize(*SCREEN_SIZE))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.get_new_level()

    def get_new_level(self):
        if game_info.info.level == 'level_1':
            new_level = 'level_2'
            game_info.info.put_new_level(new_level)
        elif game_info.info.level == 'level_2':
            new_level = 'level_3'
            game_info.info.put_new_level(new_level)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.close()
            self.main_menu = main_menu.MainMenu()
            self.main_menu.show()
