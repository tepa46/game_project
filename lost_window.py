from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt
import main_menu

SCREEN_SIZE = [700, 700]


class LostWindow(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ПОБЕДА')
        self.setFixedSize(*SCREEN_SIZE)

        oImage = QImage('lost/lost.png')
        sImage = oImage.scaled(QSize(*SCREEN_SIZE))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.close()
            self.main_menu = main_menu.MainMenu()
            self.main_menu.show()
