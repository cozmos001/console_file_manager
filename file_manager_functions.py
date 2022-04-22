import os
import shutil
import sys
import random

"""
Функция создания папки - 1
"""


def create_folder(name):
    # Проверка на существование
    if not os.path.exists(name):
        # Если не существует - создается папка
        os.mkdir(name)
        return 'Папка создана!'
    else:
        return 'Папка уже существует!'


"""
Функция удаления файла/папки - 2
"""


def delite_file_folder(name):
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
        return 'Файл/папка не найден!'


"""
Функция копирования файла/папки - 3
"""


def copy_file_folder(name, new_name):
    try:
        if os.path.isdir(name):
            shutil.copytree(name, new_name)
            return 'Папка скопирована!'
        else:
            shutil.copy(name, new_name)
            return 'Файл скопирован!'
    except FileNotFoundError:
        return 'Файл/папка не найдена!'


"""
Функция просмотра содержимого рабочей директории - 4
"""


def content():
    if len(os.listdir()) == 0:
        return 'Директория пуста!'
    else:
        return os.listdir()


"""
Функция просмотра содержимого - только папки - 5
"""


def folders_only():
    folders = []
    for obj in os.listdir():
        if os.path.isdir(obj):
            folders.append(obj)
    return folders


"""
Функция просмотра содержимого - только файлы - 6
"""


def file_only():
    file = []
    for obj in os.listdir():
        if os.path.isfile(obj):
            file.append(obj)
    return file


"""
функция вывода информации об операционной системе - 7
"""


def os_info():
    if sys.platform == 'linux' or sys.platform == 'linux2':
        return 'Linux'
    elif sys.platform == 'darwin':
        return 'OS X'
    elif sys.platform == 'win32':
        return 'Windows'


"""
Функция о создателе программы
"""


def author_info():
    return 'Author Aleksandr Tronin'


"""
Функция смены рабочей директории 
"""


def change_dir(directory):
    try:
        os.chdir(directory)
        return f'Текущая рабочая директория: {os.getcwd()}'
    except FileNotFoundError:
        return f'Директория: {directory} не существует'
    except NotADirectoryError:
        return f'{directory} не является директорией'
    except PermissionError:
        return f'У вас нет разрешений для перехода на {directory}'
