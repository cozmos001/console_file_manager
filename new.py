import os
import shutil

def create_folder(name):
    # Проверка на существование
    if not os.path.exists(name):
        # Если не существует - создается папка
        os.mkdir(name)
        return 'Папка создана!'
    else:
        return 'Папка уже существует!'

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

def content():
    if len(os.listdir()) == 0:
        return 'Директория пуста!'
    else:
        return os.listdir()
