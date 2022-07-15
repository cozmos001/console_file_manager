import os

from file_manager_functions import print_menu, create_folder, delite_file_folder, copy_file_folder, \
    content, folders_only, file_only, os_info, author_info, change_dir, separator
from my_bank import run_my_bank
from victorina import run_victorina

while True:
    print_menu()
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
        for obj in content():
            print(obj)

    elif choice == '5':
        work_dir = f'file: {file_only()}\ndirs: {folders_only()}'
        with open('listdir.txt', 'w') as f:
            f.write(work_dir)
        print('Содержимое рабочей директории сохранено в файл listdir.txt')

    elif choice == '6':
        for folder in folders_only():
            print(folder)

    elif choice == '7':
        for file in file_only():
            print(file)

    elif choice == '8':
        print(os_info())

    elif choice == '9':
        print(author_info())

    elif choice == '10':
        run_victorina()

    elif choice == '11':
        run_my_bank()

    elif choice == '12':
        print(f'Текущая рабочая директория: {os.getcwd()}')
        directory = input('Введите название директории или путь(для перехода в предыдущую введите: ..): ')
        print(change_dir(directory))

    elif choice == '13':
        break

    else:
        print('Неверный пункт меню')
