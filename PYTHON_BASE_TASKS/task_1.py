"""Задача 1: Реверсирование строки
Напишите функцию, которая принимает строку и возвращает её, но со словами в обратном порядке"""


def reverse_words(word: str) -> str:
    """Функция, принимающая на вход строку и возвращает её, но со словами в обратном порядке"""
    return ' '.join(word.split()[::-1])


if __name__ == '__main__':
    print(reverse_words('hello world'))