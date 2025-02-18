'''Задача 2: Словари и множества
Напишите функцию, которая принимает список строк и возвращает словарь,
где ключи - уникальные слова
значения — множества индексов строк, в которых эти слова встречаются.'''


def words_index_map(strings: list[str]) -> dict[str, set[int]]:
    """Функция, возвращающая словарь, где ключи - уникальные слова,
    а знаения - множества индексов строк, в которых эти слова встречаются."""
    words_index_map = {}
    for index, string in enumerate(strings):
        for word in string.split():
            if word not in words_index_map:
                words_index_map[word] = {index}
            else:
                words_index_map[word].add(index)
    return words_index_map


strings = [
    "hello world",
    "world of python",
    "hello again"
]
print(words_index_map(strings))
