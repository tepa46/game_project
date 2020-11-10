from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtWidgets import QPushButton, QApplication
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import button_config
import button_treatment
import invent
import win_window
import lost_window
import game_info
import make_history
import final_window
import os

SCREEN_SIZE = [700, 700]


class Engine(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initUI()

    def initUI(self):
        game_info.info.clear_files()

        self.setWindowTitle('Undertale')
        self.setGeometry(0, 0, *SCREEN_SIZE)
        self.setFixedSize(*SCREEN_SIZE)

        self.button_lst = list()

        self.button_lst.append(QPushButton(self))
        self.button_lst[0].clicked.connect(lambda: self.pushed_button('button_1.txt'))

        self.button_lst.append(QPushButton(self))
        self.button_lst[1].clicked.connect(lambda: self.pushed_button('button_2.txt'))

        self.button_lst.append(QPushButton(self))
        self.button_lst[2].clicked.connect(lambda: self.pushed_button('button_3.txt'))

        self.button_lst.append(QPushButton(self))
        self.button_lst[3].clicked.connect(lambda: self.pushed_button('button_4.txt'))

        self.button_lst.append(QPushButton(self))
        self.button_lst[4].clicked.connect(lambda: self.pushed_button('button_5.txt'))

        self.button_invent = QPushButton('ИНВЕНТАРЬ', self)
        self.button_invent.clicked.connect(self.invent_show)

        self.make_room(f'{game_info.info.level}/{game_info.info.file}/background.png')

    def make_room(self, text):
        self.make_background(text)
        self.make_buttons()
        self.make_room_history()

    def make_buttons(self):
        button_config.button_config(self)
        self.show()

    def make_background(self, file_name):
        oImage = QImage(file_name)
        sImage = oImage.scaled(QSize(*SCREEN_SIZE))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def make_room_history(self):
        if not game_info.info.get_used_history() and game_info.info.get_history() != 'This room has no history':
            self.make_history = make_history.HistoryWindow()
            self.make_history.show()

    def pushed_button(self, button_name):
        text, command, new_file = game_info.info.get_button_info(button_name)
        code = button_treatment.button_treatment(self, command, button_name)
        game_info.info.put_file(new_file)
        if code == 1:
            self.new_room()
        elif code == 2:
            self.do_win_window()
        elif code == 3:
            self.do_lost_window()
        elif code == 4:
            self.do_game_end_wind()

    def new_room(self):
        self.update()
        self.make_room(os.path.join(fr'{game_info.info.level}/{game_info.info.file}', 'background.png'))
        QApplication.processEvents()

    def invent_show(self):
        self.invent_view = invent.Invent()
        self.invent_view.show()

    def do_win_window(self):
        self.close()
        self.win_window = win_window.WinWindow()
        self.win_window.show()

    def do_lost_window(self):
        self.close()
        self.lost_window = lost_window.LostWindow()
        self.lost_window.show()

    def do_game_end_wind(self):
        self.close()
        self.game_end_win = final_window.FinalWindow()
        self.game_end_win.show()
