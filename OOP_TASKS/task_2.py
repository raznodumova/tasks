"""Задача 2: Создание банковской системы
Создайте систему для управления банковскими счетами.
У каждого счета должны быть атрибуты: номер счета, имя владельца, баланс.
Система должна поддерживать следующие операции:

1. Депозит средств.
2. Снятие средств.
3. Проверка баланса.
4. Перевод средств с одного счета на другой.

Используйте магические методы для вывода информации о счете
и для проверки равенства счетов (например, по номеру счета)."""

'''
Создаем класс счета
__init__ - конструктор
__str__ - метод для вывода информации о счете
__eq__ - метод для проверки равенства счетов
check_balance - метод для проверки баланса
deposit - метод для пополнения счета
withdraw - метод для снятия средств
'''


class BankAccount:
    def __init__(self, number: int, name: str, balance: int):
        self.number = number
        self.name = name
        self.balance = balance

    def __str__(self):
        return (f'Номер счета: {self.number}\n'
                f'Имя владельца: {self.name}\n'
                f'Баланс: {self.balance}')

    def __eq__(self, other: object):
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.number == other.number

    def check_balance(self):
        return self.balance

    def deposit(self, amount: int):
        if amount > 0:
            self.balance += amount
            print('Счет успешно пополнен')
        else:
            print('Сумма пополнения должна быть положительной')

    def withdraw(self, amount: int):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'Средства сняты. Текущий баланс: {self.balance}')
        else:
            print('Недостаточно средств')


'''
создаем класс банковской системы
__init__ - конструктор
add_account - метод для добавления счета в систему
transfer - метод для перевода средств между счетами
'''


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def add_account(self, BankAccount: BankAccount):
        if BankAccount.number in self.accounts:
            print('Такой счет уже существует')
        else:
            self.accounts[BankAccount.number] = BankAccount
            print('Счет успешно добавлен')

    def transfer(self, account_from: int,
                 account_to_number: int, amount: int):
        if (account_from in self.accounts
                and account_to_number in self.accounts):
            if account_from != account_to_number:
                if self.accounts[account_from].check_balance() >= amount:
                    self.accounts[account_from].withdraw(amount)
                    self.accounts[account_to_number].deposit(amount)
                    print(f'Средства переведены пользователю '
                          f'{self.accounts[account_to_number].name}')
            else:
                print('Нельзя перевести средства самому себе')


if __name__ == '__main__':
    account1 = BankAccount(12345, "Иван Иванов", 1000)
    account2 = BankAccount(67890, "Петр Петров", 2000)

    bank = BankSystem()
    bank.add_account(account1)
    bank.add_account(account2)

    account1.deposit(500)
    account2.withdraw(300)
    bank.transfer(12345, 67890, 200)

    print(account1)
    print(account2)
