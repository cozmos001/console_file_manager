import datetime
import os
import pickle

FILE_NAME_BALANCE_SAVE = 'balance.txt'
FILE_NAME_PURCHASE_SAVE = 'purchase.data'


def run_my_bank():
    money = 0
    if os.path.exists(FILE_NAME_BALANCE_SAVE):
        with open(FILE_NAME_BALANCE_SAVE, 'r') as f:
            money = int(f.read())

    list_purchase = []
    if os.path.exists(FILE_NAME_PURCHASE_SAVE):
        with open(FILE_NAME_PURCHASE_SAVE, 'rb') as f:
            list_purchase = pickle.load(f)
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'Ваш баланс {money}')

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
                        list_purchase.append(
                            [purchase, purchase_amount, datetime.datetime.now().strftime("%d/%m/%y %H:%M")])
                        money -= int(purchase_amount)

                    else:
                        print('Недостаточно денег')
                    break
                else:
                    print('Вы ввели не число')
        elif choice == '3':
            if len(list_purchase) != 0:
                for purchase, purchase_amount, date in list_purchase:
                    print(purchase, purchase_amount, date)
            else:
                print('Вы пока не совершали покупок')
        elif choice == '4':
            with open(FILE_NAME_BALANCE_SAVE, 'w') as f:
                f.write(f'{money}')
            with open(FILE_NAME_PURCHASE_SAVE, 'wb') as f:
                pickle.dump(list_purchase, f)
            break
        else:
            print('Неверный пункт меню')
