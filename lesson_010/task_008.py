class ATM:
    def __init__(self):
        self.initial_amount = 0
        self.operations_counter = 0
        self.tax_amount = 0

    def top_up(self):
        self.impossible_if_the_limit_is_exceeded()
        self.initial_amount = self.check_tax()
        self.operations_counter += 1

        summ = int(input('Введите сумму для пополнения: '))
        self.impossible_if_not_multiple_50(summ)

        self.initial_amount += summ
        self.initial_amount += summ * 0.03
        print(f'Текущий баланс:, {self.initial_amount}')

    def withdraw(self):
        self.impossible_if_the_limit_is_exceeded()
        self.initial_amount = self.check_tax()
        self.operations_counter += 1

        summ = int(input('Введите сумму для снятия: '))
        if summ > self.initial_amount:
            print('Недостаточно денег на счете')
            self.go_out()

        self.impossible_if_not_multiple_50(summ)
        commission = summ * 0.015

        if commission < 30:
            commission = 30
        if commission > 600:
            commission = 600

        self.initial_amount -= (summ + commission)
        self.initial_amount += self.initial_amount * 0.03
        print(f'Текущий баланс: {self.initial_amount}')

    def impossible_if_the_limit_is_exceeded(self):
        if self.initial_amount >= 5000000:
            self.initial_amount -= self.initial_amount * 0.1
            self.tax_amount += self.initial_amount * 0.1
            print('Невозможно! Превышен лимит!')
            self.go_out()

    def check_tax(self):
        if self.operations_counter % 3 == 0:
            self.initial_amount += self.initial_amount * 0.03
        return self.initial_amount

    def impossible_if_not_multiple_50(self, summ):
        if summ % 50 != 0:
            print('Сумма должна быть кратна 50 у.е.')
            self.go_out()

    def go_out(self):
        print('Спасибо за использование банкомата!')

    def start(self):
        while True:
            print('Выберете действие\n'
                  '1. Пополнить\n'
                  '2. Снять\n'
                  '3. Выйти')
            action = int(input())
            if action == 1:
                self.top_up()
            if action == 2:
                self.withdraw()
            if action == 3:
                self.go_out()
                break

atm = ATM()
atm.start()
