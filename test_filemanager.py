from file_manager_functions import create_folder, delite_file_folder, copy_file_folder, \
    content, folders_only, file_only, os_info, author_info, change_dir, separator
from victorina import date_to_text
import os


def test_separator():
    assert type(separator()) == str
    assert separator(3) == '***'


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


def test_folders_only():
    os.mkdir('check')  # Создаем папку
    assert type(folders_only()) == list
    assert 'check' in folders_only()
    os.rmdir('check')  # Удаляем папку


def test_file_only():
    open('check', 'w')  # Создаем файл
    assert type(file_only()) == list
    assert 'check' in file_only()
    os.remove('check')


def test_os_info():
    assert type(os_info()) == str
    assert os_info() == 'OS X'


def test_author_info():
    assert type(author_info()) == str
    assert author_info() == 'Author Aleksandr Tronin'


def test_date_to_text():
    assert date_to_text('01.06.1996') == 'первое июня 1996 года.'


def test_change_dir():
    os.mkdir('check')  # Создаем папку
    open('check1', 'w')  # Создаем файл
    assert change_dir('check') == f'Текущая рабочая директория: {os.getcwd()}'
    assert change_dir('check2') == f'Директория: check2 не существует'
    assert change_dir('..') == f'Текущая рабочая директория: {os.getcwd()}'
    assert change_dir('check1') == f'check1 не является директорией'
    os.rmdir('check')  # Удаляем папку
    os.remove('check1')
