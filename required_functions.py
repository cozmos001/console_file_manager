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
    for i in os.listdir():
        if os.path.isdir(i):
            print(i)

"""
Функция просмотра содержимого - только файлы - 6
"""
def file_only():
    for i in os.listdir():
        if os.path.isfile(i):
            print(i)
"""
функция вывода информации об операционной системе - 7
"""
def os_info():
    if sys.platform == 'linux' or sys.platform == 'linux2':
        print('Linux')
    elif sys.platform == 'darwin':
        print('OS X')
    elif sys.platform == 'win32':
        print('Windows')

"""
Функция викторины - 9
"""
def test():
    # Словарь с именами известных людей и датами их рождения
    dict_people = {
        'A_S_Pushkin': '06.06.1799',
        'John_Lennon': '09.10.1940',
        'M_Y_Lermontov': '15.10.1814',
        'Albert_Einstein': '14.03.1879',
        'Steve_Jobs': '24.02.1955',
        'Bill_Gates': '28.10.1955',
        'Yuri_Gagarin': '09.03.1934',
        'Peter_I': '09.06.1672',
        'D_I_Mendeleev': '08.02.1834',
        'F_M_Dostoevsky': '11.11.1821'
    }

    # Список известных людей(ключи из словаря)
    great_people = list(dict_people.keys())

    # Список дней прописью
    day = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
           'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое',
           'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье',
           'двадцать четвертое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое',
           'двадцать девятое', 'тридцатое', 'тридцать первое']

    # Список месяцев прописью
    month = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
             'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

    play = True
    while play == True:
        # Выбор пяти случайных людей из списка
        results = random.sample(great_people, 5)
        win = 0
        lose = 0
        for i in results:
            answer = input(f'Введите год рождения {i}(в формате - dd.mm.yyyy): ')
            if answer == dict_people[i]:
                print('Поздравляем, это правильный ответ!!!')
                win += 1
            else:
                print('Это неправильный ответ!!!')
                print('Правильный ответ: ' + ' '.join([str(day[int(dict_people[i].split('.')[0]) - 1]),
                                                       str(month[int(dict_people[i].split('.')[1]) - 1]),
                                                       dict_people[i].split('.')[2]]) + ' года')
                lose += 1
        print(f'Правельных ответов: {win}, неправильных ответов: {lose}')

        while True:
            again = input('Хотите попробовать еще раз? ')
            if 'y' in again.lower() or 'д' in again.lower():
                play = True
                break
            elif 'n' in again.lower() or 'н' in again.lower():
                play = False
                break
            else:
                print('Неизвестная команда!')

"""
Функция мой банковский счет - 10
При такой конструкции переменные money и list_purchase будут сохранены до выхода из основной программы
"""
money = 0
list_purchase = []
def my_bank(money=money, list_purchase=list_purchase):
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            while True:
                count = input('Введите сумму на которую хотите пополнить счет: ')
                if count.isdigit():
                    money += int(count)
                    break
                else:
                    print('Вы ввели не число')
        elif choice == '2':
            while True:
                purchase_amount = input('Введите сумму покупки: ')
                if purchase_amount.isdigit():
                    if int(purchase_amount) <= money:
                        purchase = input('Введите название покупки: ')
                        list_purchase.append([purchase, purchase_amount])
                        money -= int(purchase_amount)

                    else:
                        print('Недостаточно денег')
                    break
                else:
                    print('Вы ввели не число')
        elif choice == '3':
            if len(list_purchase) != 0:
                for purchase, purchase_amount in list_purchase:
                    print(purchase, purchase_amount)
            else:
                print('Вы пока не совершали покупок')
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

"""
Функция смены рабочей директории 
"""
def change_dir():
    print(f'Текущая рабочая директория: {os.getcwd()}')
    directory = input('Введите название директории или путь(для перехода в предыдущую введите: ..): ')
    try:
        os.chdir(directory)
        print(f'Текущая рабочая директория: {os.getcwd()}')
    except FileNotFoundError:
        print(f'Директория: {directory} не существует')
    except NotADirectoryError:
        print(f'{directory} не является директорией')
    except PermissionError:
        print(f'У вас нет разрешений для перехода на {directory}')

