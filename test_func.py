from new import create_folder, delite_file_folder, copy_file_folder, content
import os

def test_create_folder():
    assert create_folder('prob') == 'Папка создана!'
    assert 'prob' in os.listdir()
    assert create_folder('prob') == 'Папка уже существует!'
    os.rmdir('prob')

def test_delite_file_folder():
    os.mkdir('check')  # Создаем папку
    open('check/check', 'w')  # Создаем файл в этой папке
    assert delite_file_folder('check') == 'Папка не пуста!'  # Пробуем удалить папку
    assert delite_file_folder('check/check') == 'Файл удален!'  # Удаляем файл
    assert 'check' not in os.listdir('check/')  # Проверка на наличие удаленного файла
    assert delite_file_folder('check/check') == 'Файл/папка не найден!'  # # Проверка на наличие удаленного файла
    assert delite_file_folder('check') == 'Папка удалена!'  # Удаляем папку
    assert 'check' not in os.listdir()  # Проверка на наличие удаленной папки
    assert delite_file_folder('check')  # Проверка на наличие удаленной папки

def test_copy_file_folder():
    os.mkdir('check')  # Создаем папку
    assert copy_file_folder('check', 'check_copy') == 'Папка скопирована!'
    assert 'check_copy' in os.listdir()
    os.rmdir('check')
    os.rmdir('check_copy')
    open('check', 'w')  # Создаем файл
    assert copy_file_folder('check', 'check_copy') == 'Файл скопирован!'
    assert 'check_copy' in os.listdir()
    os.remove('check')
    os.remove('check_copy')
    assert copy_file_folder('check', 'check_copy') == 'Файл/папка не найдена!'

def test_content():
    os.mkdir('check')  # Создаем папку
    assert type(content()) == list
    os.chdir('check/')
    assert content() == 'Директория пуста!'
    os.chdir('..')
    os.rmdir('check')  # Удаляем папку
