from PyQt5.QtWidgets import QInputDialog
import challenge_window
import game_info

CHALLENGE_SCREEN_SIZE = [280, 100]

SCREEN_SIZE = [700, 700]


def chall_window(self):
    self.challenge_window = challenge_window.ChallengeWindow()
    self.challenge_window.show()


def check(self, button_name):
    chall_list = game_info.info.challenge
    text = game_info.info.get_button_file(button_name)
    completed_tasks_lst = game_info.info.completed_tasks

    if text[4] not in completed_tasks_lst:

        game_info.info.put_completed_tasks(text)
        if chall_list[int(text[4]) - 1] != '':
            game_info.info.put_inventory(text)

        game_info.info.put_sequence_new(text)
    else:
        game_info.info.put_sequence_old()

    chall_window(self)


def button_treatment(self, command, button_name):
    ans = game_info.info.answer
    if command == 'ОБРАТНО' or command == 'ВОЙТИ В КОМНАТУ' or command == 'ПРОЙТИ ДАЛЬШЕ':
        return 1
    elif command == 'ПОСМОТРЕТЬ':
        check(self, button_name)
    elif command == 'ВЫБРАТЬСЯ ИЗ УБЕЖИЩА':
        password, ok_pressed = QInputDialog.getText(self, "Код доступа",
                                                    "Какой код доступа?")
        if ok_pressed:
            if password == ans:
                return 4
            return 3
    elif command == 'ПРЕДОСТАВИТЬ ПАРОЛЬ':
        password, ok_pressed = QInputDialog.getText(self, "Код доступа",
                                                    "Какой код доступа?")
        if ok_pressed:
            if password == ans:
                return 2
            return 3
