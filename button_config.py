import game_info


def button_set(self, level, file, num):
    with open(f'{level}/{file}/button_{num}.txt', 'r', encoding='utf8') as input_file:
        text = input_file.read()

        self.button_lst[num - 1].move(int(text.split('\n')[0].split(' ')[0]),
                                      int(text.split('\n')[0].split(' ')[1]))
        self.button_lst[num - 1].resize(int(text.split('\n')[1].split(' ')[0]),
                                        int(text.split('\n')[1].split(' ')[1]))
        self.button_lst[num - 1].setText(text.split('\n')[2])


def button_config(self):
    level = game_info.info.level
    file = game_info.info.file
    for num in range(1, 6):
        button_set(self, level, file, num)

    self.button_invent.move(0, 900)
    self.button_invent.resize(100, 100)
