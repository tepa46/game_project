from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QWidget
import game_info

CHALLENGE_SCREEN_SIZE = [280, 100]


def is_new_num(sequence_text):
    if sequence_text != 'Вы уже тут все посмотрели' and sequence_text != 'Здесь ничего нет':
        return True
    return False


class ChallengeWindow(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Challenge')
        self.setGeometry(300, 300, *CHALLENGE_SCREEN_SIZE)
        self.setFixedSize(*CHALLENGE_SCREEN_SIZE)

        self.label = QLabel(self)

        sequence_text = game_info.info.sequence_text
        if is_new_num(sequence_text):
            self.label.setText('Вы нашли новую часть последовательности: ' + '\n' + sequence_text)
        else:
            self.label.setText(sequence_text)
        self.label.move(20, 20)

        self.btn = QPushButton('OK', self)
        self.btn.move(100, 70)
        self.btn.clicked.connect(self.close_window)

    def close_window(self):
        self.close()
