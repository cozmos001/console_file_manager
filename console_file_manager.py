"""
2. В проекте реализовать следующий функционал:
После запуска программы пользователь видит меню, состоящее из следующих пунктов:
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.
Так же можно добавить любой дополнительный функционал по желанию.
"""

from file_manager_functions import create_folder, delite_file_folder, copy_file_folder, \
    content, folders_only, file_only, os_info, author_info, change_dir
from victorina import run_victorina
from my_bank import run_my_bank
import os

while True:
    print('1 - создать папку')
    print('2 - удалить (файл/папку)')
    print('3 - копировать (файл/папку)')
    print('4 - просмотр содержимого рабочей директории')
    print('5 - посмотреть только папки')
    print('6 - посмотреть только файлы')
    print('7 - просмотр информации об операционной системе')
    print('8 - создатель программы')
    print('9 - играть в викторину')
    print('10 - мой банковский счет')
    print('11 - смена рабочей директории')
    print('12 - выход')

    choice = input('Выберите пункт меню: ')

    if choice == '1':
        name = input('Введите название папки: ')
        print(create_folder(name))

    elif choice == '2':
        name = input('Введите название файла/папки для удаления: ')
        print(delite_file_folder(name))

    elif choice == '3':
        name = input('Введите имя файла/папки: ')
        new_name = input('Введите новое название: ')
        print(copy_file_folder(name, new_name))

    elif choice == '4':
        print(content())

    elif choice == '5':
        print(folders_only())

    elif choice == '6':
        print(file_only())

    elif choice == '7':
        print(os_info())

    elif choice == '8':
        print(author_info())

    elif choice == '9':
        run_victorina()

    elif choice == '10':
        run_my_bank()

    elif choice == '11':
        print(f'Текущая рабочая директория: {os.getcwd()}')
        directory = input('Введите название директории или путь(для перехода в предыдущую введите: ..): ')
        print(change_dir(directory))

    elif choice == '12':
        break

    else:
        print('Неверный пункт меню')
