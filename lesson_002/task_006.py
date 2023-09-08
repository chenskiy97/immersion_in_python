"""
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""


def top_up():
    global initial_amount, operations_counter, tax_amount

    impossible_if_the_limit_is_exceeded()
    initial_amount = check_tax()
    operations_counter += 1

    summ = int(input('Введите сумму для пополнения: '))
    impossible_if_not_multiple_50(summ)

    initial_amount += summ
    initial_amount += summ * 0.03
    print(f'Текущий баланс:, {initial_amount}')


def withdraw():
    global initial_amount, operations_counter, tax_amount

    impossible_if_the_limit_is_exceeded()
    initial_amount = check_tax()
    operations_counter += 1

    summ = int(input('Введите сумму для снятия: '))
    if summ > initial_amount:
        print('Недостаточно денег на счете')
        go_out()

    impossible_if_not_multiple_50(summ)
    commission = summ * 0.015

    if commission < 30:
        commission = 30
    if commission > 600:
        commission = 600

    initial_amount -= (summ + commission)
    initial_amount += initial_amount * 0.03
    print(f'Текущий баланс: {initial_amount}')


def impossible_if_the_limit_is_exceeded():
    global initial_amount, tax_amount
    if initial_amount >= 5000000:
        initial_amount -= initial_amount * 0.1
        tax_amount += initial_amount * 0.1
        print('Невозможно! Превышен лимит!')
        go_out()


def check_tax():
    global initial_amount, operations_counter
    if operations_counter % 3 == 0:
        initial_amount += initial_amount * 0.03
    return initial_amount


def impossible_if_not_multiple_50(summ):
    if summ % 50 != 0:
        print('Сумма должна быть кратна 50 у.е.')
        go_out()


def go_out():
    print('Спасибо за использование банкомата!')


initial_amount = 0
operations_counter = 0
tax_amount = 0

while True:
    print('Выберете действие\n'
          '1. Пополнить\n'
          '2. Снять\n'
          '3. Выйти')
    action = int(input())
    if action == 1:
        top_up()
    if action == 2:
        withdraw()
    if action == 3:
        go_out()
        break
