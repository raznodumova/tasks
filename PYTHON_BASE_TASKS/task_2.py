"""Задача 3: Частота символов
Напишите функцию, которая принимает строку и возвращает словарь,
где ключами являются символы, а значениями — их частота в строке."""

from collections import Counter


def char_frequency(word: str) -> dict:
    """Функция, возвращающая словарь, где ключами являются символы, а значениями — их частота в строке."""
    return dict(Counter(word))


if __name__ == '__main__':
    print(char_frequency('hello world'))