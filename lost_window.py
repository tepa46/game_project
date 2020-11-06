from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt
import mainmenu

SCREEN_SIZE = [1000, 1000]


class Lost_window(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ПОБЕДА')
        self.setGeometry(0, 0, *SCREEN_SIZE)

        oImage = QImage('lost/lost.png')
        sImage = oImage.scaled(QSize(*SCREEN_SIZE))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.close()
            self.main_menu = mainmenu.MainMenu()
            self.main_menu.show()
