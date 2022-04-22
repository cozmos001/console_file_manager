def run_my_bank():
    money = 0
    list_purchase = []
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
