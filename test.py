"""Задача 1: Реверсирование строки
Напишите функцию, которая принимает строку и возвращает её, но со словами в обратном порядке"""


def reverse_words(s: str) -> str:
    string = s.split()
    return ' '.join(string[::-1])


if __name__ == '__main__':
    print(reverse_words('hello world'))

"""Задача 3: Частота символов
Напишите функцию, которая принимает строку и возвращает словарь, 
где ключами являются символы, а значениями — их частота в строке."""


def char_frequency(s: str) -> dict:
    return dict((i, s.count(i)) for i in s)


if __name__ == '__main__':
    print(char_frequency('hello world'))