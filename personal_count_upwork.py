import os
import pickle


count = 0
history = []
count_file = ('count_start.txt')
temp = ''
history_memory = 'history_file.data'
if os.path.exists(history_memory):
    with open(history_memory, 'rb') as f:
        history = pickle.load(f)

if os.path.exists(count_file):
    with open('count_start.txt', 'r') as count_file:
        result = count_file.read()
        for i in result:
                if i.isdigit():
                    temp = temp + i
    count = int(temp)


def refill(count_zero):
    e = int(input('Введите сумму, на которую вы хотите пополнить счет: '))
    count_zero = count_zero + e
    print(f'На вашем счету {count_zero} рублей')
    return count_zero


def purchase(count_zero, history_zero):
    sum_of_purchase = input('Введите сумму покупки: ')
    if sum_of_purchase.isdigit():
        sum_of_purchase = int(sum_of_purchase)
        if sum_of_purchase > count_zero:
            print('Недостаточно средств')
        else:
            purchase = input('Введите наименование покупки: ')
            count_zero = count_zero - sum_of_purchase
            purch = (purchase, sum_of_purchase)
            history_zero.append(purch)
            print(f'У вас осталось {count_zero} рублей')
    else:
        print('Неверный ввод!')
    return count_zero, history_zero


def print_history(history_zero):
    print('История покупок: ')
    for i in history_zero:
        print(f'Покупка: {i[0]} Цена: {i[1]}')


while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        count = refill(count)
    elif choice == '2':
        count, history = purchase(count, history)
    elif choice == '3':
        print_history(history)
    elif choice == '4':
        count_file = open('count_start.txt', 'w')
        count_file.write(str(count))
        count_file.close()
        print(history)
        with open(history_memory, 'wb') as f:
            pickle.dump(history, f)
        break
    else:
        print('Неверный пункт меню')