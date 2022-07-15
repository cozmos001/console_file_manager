import os
import shutil
import sys

CREATE_FOLDER = 'создать папку'
DELETE_FILE_FOLDER = 'удалить (файл/папку)'
COPY_FILE_FOLDER = 'копировать (файл/папку)'
SHOW_CONTENT = 'просмотр содержимого рабочей директории'
SAVE_CONTENT_IN_FILE = 'сохранить содержимое рабочей директории в файл'
SHOW_FOLDERS = 'посмотреть только папки'
SHOW_FILES = 'посмотреть только файлы'
INFO_OS = 'просмотр информации об операционной системе'
INFO_AUTOR = 'создатель программы'
VICTORY = 'играть в викторину'
MY_BANK = 'мой банковский счет'
CHANG_DIR = 'смена рабочей директории'
EXIT = 'выход'

menu_items = (
    CREATE_FOLDER,
    DELETE_FILE_FOLDER,
    COPY_FILE_FOLDER,
    SHOW_CONTENT,
    SAVE_CONTENT_IN_FILE,
    SHOW_FOLDERS,
    SHOW_FILES,
    INFO_OS,
    INFO_AUTOR,
    VICTORY,
    MY_BANK,
    CHANG_DIR,
    EXIT
)

'''
Декоратор для меню
'''


def add_separator(func):
    def inner(*args, **kwargs):
        print('*' * 30)
        result = func(*args, **kwargs)
        print('*' * 30)
        return result

    return inner


def separator(count=30):
    """
    Функция разделитель
    :param count: количество '*' в разделителе
    :return: строка с '*' в зависимости от count
    """
    return '*' * count


"""
Функция вывода меню

Альтернативный вариант функции с выводом меню
def print_menu():
    print(separator())
    print('1 - создать папку')
    print('2 - удалить (файл/папку)')
    print('3 - копировать (файл/папку)')
    print('4 - просмотр содержимого рабочей директории')
    print('5 - сохранить содержимое рабочей директории в файл')
    print('6 - посмотреть только папки')
    print('7 - посмотреть только файлы')
    print('8 - просмотр информации об операционной системе')
    print('9 - создатель программы')
    print('10 - играть в викторину')
    print('11 - мой банковский счет')
    print('12 - смена рабочей директории')
    print('13 - выход')
    print(separator())
"""


@add_separator
def print_menu():
    """
    Функция вывода меню
    Выводит название пункта меню и порядковый номер
    :return: None
    """
    for number, item in enumerate(menu_items, 1):
        print(f'{number} - {item}')


"""
Вариант с проверкой на существование

def create_folder(name):
    '''
    Функция создания папки 
    :param name: имя создаваемой папки
    :return: Сообщение: Папка создана! или Папка уже существует!
    '''
    # Проверка на существование
    if not os.path.exists(name):
        # Если не существует - создается папка
        os.mkdir(name)
        return 'Папка создана!'
    else:
        return 'Папка уже существует!'
"""


def create_folder(name):
    """
    Функция создания папки
    :param name: имя создаваемой папки
    :return: Сообщение: Папка создана! или Папка уже существует!
    """
    try:
        os.mkdir(name)
        return 'Папка создана!'
    except FileExistsError:
        return 'Папка уже существует!'


def delite_file_folder(name):
    """
    Функция удаления файла/папки
    :param name: имя файла/папки
    :return: Сообщение 'Папка удалена!' если папка удалена
             Сообщение 'Папка не пуста!' если папка не пуста
             Сообщение 'Файл удален!' если файл удален
             Сообщение 'Файл/папка не найден!' если файл/папка не найдены
    """
    if os.path.isdir(name):
        try:
            os.rmdir(name)
            return 'Папка удалена!'
        except OSError:
            return 'Папка не пуста!'
    elif os.path.isfile(name):
        os.remove(name)
        return 'Файл удален!'
    else:
        return 'Файл/папка не найдены!'


def copy_file_folder(name, new_name):
    """
    Функция копирования файла/папки
    :param name: Имя файла/папки которую надо скопировать
    :param new_name: Новое имя файла/папки
    :return: Сообщение 'Папка скопирована!' если папка скопирована
             Сообщение 'Файл скопирован!' если файл скопирован
             Сообщение 'Файл/папка не найден!' если файл/папка не найдены
    """
    try:
        if os.path.isdir(name):
            shutil.copytree(name, new_name)
            return 'Папка скопирована!'
        else:
            shutil.copy(name, new_name)
            return 'Файл скопирован!'
    except FileNotFoundError:
        return 'Файл/папка не найдены!'


def content():
    """
    Функция просмотра содержимого рабочей директории
    :return: Сообщение 'Директория пуста!' если директория пуста
             Содержимое рабочей директории если в ней что-то есть
    """
    if len(os.listdir()) == 0:
        return 'Директория пуста!'
    else:
        return os.listdir()


def folders_only():
    """
    Функция просмотра содержимого - только папки
    :return: Списое с папками в рабочей директории
    """
    folders = []
    for obj in os.listdir():
        if os.path.isdir(obj):
            folders.append(obj)
    return folders


def file_only():
    """
    Функция просмотра содержимого - только файлы
    :return: Список с файлами в рабочей директории
    """
    file = []
    for obj in os.listdir():
        if os.path.isfile(obj):
            file.append(obj)
    return file


def os_info():
    """
    Функция вывода информации об операционной системе
    :return: Сообщение 'Linux' если операционная система Lunux
             Сообщение 'OS X' если операционная система OS X
             Сообщение 'Windows' если операционная система Windows
    """
    if sys.platform == 'linux' or sys.platform == 'linux2':
        return 'Linux'
    elif sys.platform == 'darwin':
        return 'OS X'
    elif sys.platform == 'win32':
        return 'Windows'


def author_info():
    """
    Функция о создателе программы
    :return: Сообщение 'Author Aleksandr Tronin'
    """
    return 'Author Aleksandr Tronin'


def change_dir(directory):
    """
    Функция смены рабочей директории
    :param directory: Директория в которую надо перейти
    :return: Сообщение 'Текущая рабочая директория:' и имя директории
             Сообщение 'Директория: {directory} не существует' если дирректория не существует
             Сообщение '{directory} не является директорией' если дирректория не является директорией
             Сообщение 'У вас нет разрешений для перехода на {directory}' если нет разрешения для перехода
    """
    try:
        os.chdir(directory)
        return f'Текущая рабочая директория: {os.getcwd()}'
    except NotADirectoryError:
        return f'{directory} не является директорией'
    except PermissionError:
        return f'У вас нет разрешений для перехода на {directory}'
    except FileNotFoundError:
        return f'Директория: {directory} не существует'