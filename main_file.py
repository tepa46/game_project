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

SCREEN_SIZE = [1000, 1000]


class Window(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initUI()

    def initUI(self):
        game_info.clear_files()

        self.setWindowTitle('Undertale')
        self.setGeometry(0, 0, *SCREEN_SIZE)

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

        self.make_room(f'{game_info.get_level()}/{game_info.get_file()}/background.png')

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
        if not game_info.get_used_history() and game_info.get_history() != 'This room has no history':
            self.make_history = make_history.History_window()
            self.make_history.show()

    def pushed_button(self, button_name):
        text, command, new_file = game_info.get_button_info(button_name)
        code = button_treatment.button_treatment(self, command, button_name)
        game_info.put_file(new_file)
        if code == 1:
            self.new_room()
        elif code == 2:
            self.do_win_window()
        elif code == 3:
            self.do_lost_window()

    def new_room(self):
        self.update()
        self.make_room(f'{game_info.get_level()}/{game_info.get_file()}/background.png')
        QApplication.processEvents()

    def invent_show(self):
        self.invent_view = invent.Invent()
        self.invent_view.show()

    def do_win_window(self):
        self.close()
        self.win_window = win_window.Win_window()
        self.win_window.show()

    def do_lost_window(self):
        self.close()
        self.lost_window = lost_window.Lost_window()
        self.lost_window.show()
