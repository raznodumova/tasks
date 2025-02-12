'''Задача 2: Словари и множества
Напишите функцию, которая принимает список строк и возвращает словарь,
где ключи - уникальные слова
значения — множества индексов строк, в которых эти слова встречаются.'''


def words_index_map(strings: list[str]) -> dict[str, set[int]]:
    """words_index_map - возвращаемый словарь
    enumerate - забирает индекс строки и саму строку из подаваемого списка
    циклом проходим по строкам и разбиваем их на слова
    проверяем нет ли такого слова в словаре
    если нет, то добавляем его в словарь
    если есть, то добавляем индекс строки в множество"""
    words_index_map = {}
    for index, string in enumerate(strings):
        for word in string.split():
            if word not in words_index_map:
                words_index_map[word] = {index}
            else:
                words_index_map[word].add(index)
    return words_index_map


# Тест
strings = [
    "hello world",
    "world of python",
    "hello again"
]
print(words_index_map(strings))
# {'hello': {0, 2}, 'world': {0, 1}, 'of': {1}, 'python': {1}, 'again': {2}}
