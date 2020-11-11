def clear_file(name):
    with open(name, 'w') as input_file:
        input_file.truncate()


class GameInfo:
    def __init__(self):
        self.level = ''
        self.file = ''
        self.inventory = ''
        self.answer = ''
        self.challenge = ''
        self.completed_tasks = ''
        self.sequence_text = ''
        self.unlock_levels = list()

    def init_all_info(self):
        self.level = self.get_level()
        self.file = self.get_file()
        self.inventory = self.get_inventory()
        self.answer = self.get_answer()
        self.challenge = self.get_challenge()
        self.completed_tasks = self.get_completed_tasks()
        self.sequence_text = self.get_sequence_text()
        self.get_unlock_levels()

    def get_unlock_levels(self):
        with open('unlock_levels.txt', 'r', encoding='utf8') as input_file:
            self.unlock_levels = input_file.read().split('\n')

    def get_level(self):
        with open('level_num.txt', 'r') as input_file:
            return input_file.readline()

    def get_file(self):
        with open(f'{self.level}/file.txt', 'r') as input_file:
            return input_file.readline()

    def get_inventory(self):
        with open(f'{self.level}/inventory.txt', 'r') as input_file:
            return input_file.read().split('\n')

    def get_answer(self):
        with open(f'{self.level}/answer.txt', 'r', encoding='utf8') as input_file:
            return input_file.readline()

    def get_challenge(self):
        with open(f'{self.level}/challenge.txt', 'r', encoding='utf8') as input_file:
            return input_file.read().split('\n')

    def get_completed_tasks(self):
        with open(f'{self.level}/completed_tasks.txt', 'r') as input_file:
            return input_file.read().split()

    def get_sequence_text(self):
        with open(f'{self.level}/sequence_text.txt', 'r', encoding='utf8') as input_file:
            return input_file.read()

    def get_button_info(self, button_name):
        with open(f'{self.level}/{self.file}/{button_name}', 'r', encoding='utf8') as input_file:
            text = input_file.read()
            command = text.split('\n')[2]
            new_file = text.split('\n')[3]
            return text, command, new_file

    def get_button_file(self, button_name):
        with open(f'{self.level}/{self.file}/{button_name}', 'r', encoding='utf8') as input_file:
            return input_file.read().split('\n')

    def get_history(self):
        self.put_used_history()
        with open(f'{self.level}/{self.file}/room_history.txt', 'r', encoding='utf8') as input_file:
            history = input_file.read()
        return history

    def get_used_history(self):
        with open(f'{self.level}/rooms_history_used.txt', 'r', encoding='utf8') as input_file:
            used_his = input_file.read().split('\n')
        if self.file in used_his:
            return True
        return False

    def put_level(self, level):
        clear_file('level_num.txt')
        with open('level_num.txt', 'a') as output_file:
            output_file.write(level)
        self.level = self.get_level()

    def put_file(self, file):
        clear_file(f'{self.level}/file.txt')
        with open(f'{self.level}/file.txt', 'a') as output_file:
            output_file.write(file)
        self.file = self.get_file()

    def put_completed_tasks(self, text):
        with open(f'{self.get_level()}/completed_tasks.txt', 'a') as output_file:
            output_file.write(text[4] + '\n')
        self.completed_tasks = self.get_completed_tasks()

    def put_inventory(self, text):
        with open(f'{self.get_level()}/inventory.txt', 'a') as output_file:
            output_file.write(self.get_challenge()[int(text[4]) - 1] + '\n')
        self.inventory = self.get_inventory()

    def put_sequence_new(self, text):
        with open(f'{self.get_level()}/sequence_text.txt', 'w', encoding='utf8') as output_file:
            clear_file(f'{self.get_level()}/sequence_text.txt')
            if self.get_challenge()[int(text[4]) - 1] != '':
                output_file.write(self.get_challenge()[int(text[4]) - 1])
            else:
                output_file.write('Здесь ничего нет')
        self.sequence_text = self.get_sequence_text()

    def put_sequence_old(self):
        with open(f'{self.level}/sequence_text.txt', 'w', encoding='utf8') as output_file:
            clear_file(f'{self.get_level()}/sequence_text.txt')
            output_file.write('Вы уже тут все посмотрели')
        self.sequence_text = self.get_sequence_text()

    def put_used_history(self):
        with open(f'{self.level}/rooms_history_used.txt', 'a') as output_file:
            output_file.write(f'{self.file}' + '\n')

    def put_new_level(self, level_name):
        if level_name not in self.unlock_levels:
            with open('unlock_levels.txt', 'a') as output_file:
                output_file.write('\n' + level_name)

    def clear_files(self):
        clear_file(f'{self.get_level()}/inventory.txt')
        clear_file(f'{self.get_level()}/completed_tasks.txt')
        clear_file(f'{self.get_level()}/rooms_history_used.txt')


info = GameInfo()
