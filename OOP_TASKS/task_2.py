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


class BankAccount:
    """Создаем класс счета."""
    def __init__(self, number: int, name: str, balance: int):
        """Конструктор счета."""
        self.number = number
        self.name = name
        self.balance = balance

    def __str__(self):
        """Вывод информации о счете."""
        return (f'Номер счета: {self.number}\n'
                f'Имя владельца: {self.name}\n'
                f'Баланс: {self.balance}')

    def __eq__(self, other: object):
        """Проверка равенства счетов."""
        if not isinstance(other, BankAccount):
            return NotImplemented
        return self.number == other.number

    def check_balance(self):
        """Проверка баланса."""
        return self.balance

    def deposit(self, amount: int):
        """Метод для пополнения счета."""
        if amount > 0:
            self.balance += amount
            print('Счет успешно пополнен')
        else:
            raise ValueError('Сумма пополнения должна быть больше нуля')

    def withdraw(self, amount: int):
        """Метод для снятия средств."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'Средства сняты. Текущий баланс: {self.balance}')
        else:
            raise ValueError('Недостаточно средств')


class BankSystem:
    """Создаем банковскую систему."""
    def __init__(self):
        """Конструктор банковской системы."""
        self.accounts = {}

    def add_account(self, account: BankAccount):
        """Метод для добавления счета."""
        if BankAccount.number in self.accounts:
            print('Такой счет уже существует')
        else:
            self.accounts[account.number] = BankAccount
            print('Счет успешно добавлен')

    def check_account(self, number: int):
        """Метод для проверки счета."""
        if number in self.accounts:
            return number
        else:
            raise ValueError('Такого счета не существует')

    def transfer(self, account_from: int,
                 account_to_number: int, amount: int):
        """Метод для перевода средств."""
        if self.check_account(account_from) and self.check_account(account_to_number):
            if amount > 0 and amount <= self.accounts[account_from].balance:
                self.accounts[account_from].withdraw(amount)
                self.accounts[account_to_number].deposit(amount)
            else:
                raise ValueError('Ошибка при переводе средств. Недостаточно средств.')


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
