from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtWidgets import QPushButton, QApplication
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import win_window
import game_info
import make_history

SCREEN_SIZE = [700, 700]


class FinalWindow(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Game end')
        self.setFixedSize(*SCREEN_SIZE)

        game_info.info.put_level('game_end')
        game_info.info.put_file('room_1')

        self.btn = QPushButton('ЗАВЕРШИТЬ ИГРУ', self)
        self.btn.resize(120, 84)
        self.btn.move(290, 560)
        self.btn.clicked.connect(self.end_game)

        oImage = QImage(f'{game_info.info.level}/{game_info.info.file}/background.png')
        sImage = oImage.scaled(QSize(*SCREEN_SIZE))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)



    def end_game(self):
        self.close()
        self.win_window = win_window.WinWindow()
        self.win_window.show()
        self.close()
        self.history = make_history.HistoryWindow()
        self.history.show()
