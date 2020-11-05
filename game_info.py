import os


def get_level():
    with open('level_num.txt', 'r') as input_file:
        return input_file.readline()


def get_file():
    level = get_level()
    with open(f'{level}/file.txt', 'r') as input_file:
        return input_file.readline()


def get_inventory():
    with open(f'{get_level()}/inventory.txt', 'r') as input_file:
        return input_file.read().split('\n')


def get_answer():
    with open(f'{get_level()}/answer.txt', 'r', encoding='utf8') as input_file:
        return input_file.readline()


def get_challenge():
    with open(f'{get_level()}/challenge.txt', 'r', encoding='utf8') as input_file:
        return input_file.read().split('\n')


def put_level(level):
    os.system(r'nul>level_num.txt')
    with open('level_num.txt', 'a') as output_file:
        output_file.write(f'level_{level}')


def get_button_file(button_name):
    with open(f'{get_level()}/{get_file()}/{button_name}', 'r', encoding='utf8') as input_file:
        return input_file.read().split('\n')


def get_completed_tasks():
    with open(f'{get_level()}/completed_tasks.txt', 'r') as input_file:
        return input_file.read().split()


def get_sequence_text():
    with open(f'{get_level()}/sequence_text.txt', 'r', encoding='utf8') as input_file:
        return input_file.read()


def put_file(file):
    level = get_level()
    os.system(fr'nul>{level}/file.txt')
    with open(f'{level}/file.txt', 'a') as output_file:
        output_file.write(file)


def put_completed_tasks(text):
    with open(f'{get_level()}/completed_tasks.txt', 'a') as output_file:
        output_file.write(text[4] + '\n')


def put_inventory(text):
    with open(f'{get_level()}/inventory.txt', 'a') as output_file:
        output_file.write(get_challenge()[int(text[4]) - 1] + '\n')


def put_sequence_new(text):
    with open(f'{get_level()}/sequence_text.txt', 'w', encoding='utf8') as output_file:
        os.system(fr'nul>{get_level()}/sequence_text.txt')
        if get_challenge()[int(text[4]) - 1] != '':
            output_file.write(get_challenge()[int(text[4]) - 1])
        else:
            output_file.write('Здесь ничего нет')


def put_sequence_old(text):
    with open(f'{get_level()}/sequence_text.txt', 'w', encoding='utf8') as output_file:
        os.system(fr'nul>{get_level()}/sequence_text.txt')
        output_file.write('Вы уже тут все посмотрели')


def clear_files():
    os.system(fr'nul>{get_level()}/inventory.txt')
    os.system(fr'nul>{get_level()}/completed_tasks.txt')