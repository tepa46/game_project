import sys
import os
from PyQt5.QtWidgets import QInputDialog, QDialog
from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton, QApplication
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize
import time
import challenge_window

CHALLENGE_SCREEN_SIZE = [280, 100]

sequence_text = ''

with open('answer.txt', 'r', encoding='utf8') as input_file:
    ans = input_file.readline()
with open('challenge.txt', 'r', encoding='utf8') as input_file:
    chall_list = input_file.read().split('\n')
SCREEN_SIZE = [1000, 1000]


def button_treatment(self, command, in_file, file):
    if command == 'ОБРАТНО' or command == 'ВОЙТИ В КОМНАТУ':
        return 1
    else:
        if command == 'ПОСМОТРЕТЬ':

            with open(in_file, 'r', encoding='utf8') as input_file:
                text = input_file.read().split('\n')

            global sequence_text

            with open('completed_tasks.txt', 'r') as input_file:
                completed_tasks_lst = input_file.read().split()

            if text[4] not in completed_tasks_lst:

                with open('completed_tasks.txt', 'a') as output_file:
                    output_file.write(text[4] + '\n')

                if chall_list[int(text[4]) - 1] != '':
                    with open('inventory.txt', 'a') as output_file:
                        output_file.write(chall_list[int(text[4]) - 1] + '\n')

                with open('sequence_text.txt', 'w', encoding='utf8') as output_file:
                    os.system(r'nul>sequence_text.txt')

                    if chall_list[int(text[4]) - 1] != '':
                        output_file.write(chall_list[int(text[4]) - 1])
                    else:
                        output_file.write('Здесь ничего нет')

                self.challenge_window = challenge_window.Challenge_window()
                self.challenge_window.show()
            else:
                with open('sequence_text.txt', 'w', encoding='utf8') as output_file:
                    os.system(r'nul>sequence_text.txt')
                    output_file.write('Вы уже тут все посмотрели')

                self.challenge_window = challenge_window.Challenge_window()
                self.challenge_window.show()
        else:
            password, ok_pressed = QInputDialog.getText(self, "Код доступа",
                                                        "Какой код дотупа?")
            if ok_pressed:
                if password == ans:
                    return 2
                else:
                    return 3
