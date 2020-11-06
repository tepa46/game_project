from PyQt5.QtWidgets import QInputDialog
import challenge_window
import game_info

CHALLENGE_SCREEN_SIZE = [280, 100]

SCREEN_SIZE = [1000, 1000]


def chall_window(self):
    self.challenge_window = challenge_window.Challenge_window()
    self.challenge_window.show()


def check(self, button_name):
    chall_list = game_info.get_challenge()
    text = game_info.get_button_file(button_name)
    completed_tasks_lst = game_info.get_completed_tasks()

    if text[4] not in completed_tasks_lst:

        game_info.put_completed_tasks(text)
        if chall_list[int(text[4]) - 1] != '':
            game_info.put_inventory(text)

        game_info.put_sequence_new(text)
    else:
        game_info.put_sequence_old(text)

    chall_window(self)


def button_treatment(self, command, button_name):
    ans = game_info.get_answer()
    if command == 'ОБРАТНО' or command == 'ВОЙТИ В КОМНАТУ':
        return 1
    if command == 'ПОСМОТРЕТЬ':
        check(self, button_name)
    else:
        password, ok_pressed = QInputDialog.getText(self, "Код доступа",
                                                    "Какой код дотупа?")
        if ok_pressed:
            if password == ans:
                return 2
            return 3
