def button_config(self, file):
    with open(f'{file}/button_1.txt', 'r', encoding='utf8') as input_file:
        text = input_file.read()

        self.button_1.move(int(text.split('\n')[0].split(' ')[0]),
                           int(text.split('\n')[0].split(' ')[1]))
        self.button_1.resize(int(text.split('\n')[1].split(' ')[0]),
                             int(text.split('\n')[1].split(' ')[1]))
        self.button_1.setText(text.split('\n')[2])

    with open(f'{file}/button_2.txt', 'r', encoding='utf8') as input_file:
        text = input_file.read()

        self.button_2.move(int(text.split('\n')[0].split(' ')[0]),
                           int(text.split('\n')[0].split(' ')[1]))
        self.button_2.resize(int(text.split('\n')[1].split(' ')[0]),
                             int(text.split('\n')[1].split(' ')[1]))
        self.button_2.setText(text.split('\n')[2])

    with open(f'{file}/button_3.txt', 'r', encoding='utf8') as input_file:
        text = input_file.read()

        self.button_3.move(int(text.split('\n')[0].split(' ')[0]),
                           int(text.split('\n')[0].split(' ')[1]))
        self.button_3.resize(int(text.split('\n')[1].split(' ')[0]),
                             int(text.split('\n')[1].split(' ')[1]))
        self.button_3.setText(text.split('\n')[2])

    with open(f'{file}/button_4.txt', 'r', encoding='utf8') as input_file:
        text = input_file.read()

        self.button_4.move(int(text.split('\n')[0].split(' ')[0]),
                           int(text.split('\n')[0].split(' ')[1]))
        self.button_4.resize(int(text.split('\n')[1].split(' ')[0]),
                             int(text.split('\n')[1].split(' ')[1]))
        self.button_4.setText(text.split('\n')[2])

    with open(f'{file}/button_5.txt', 'r', encoding='utf8') as input_file:
        text = input_file.read()

        self.button_5.move(int(text.split('\n')[0].split(' ')[0]),
                           int(text.split('\n')[0].split(' ')[1]))
        self.button_5.resize(int(text.split('\n')[1].split(' ')[0]),
                             int(text.split('\n')[1].split(' ')[1]))
        self.button_5.setText(text.split('\n')[2])

    self.button_invent.move(0, 900)
    self.button_invent.resize(100, 100)
