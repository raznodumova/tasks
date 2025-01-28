'''Задача 1: Проверка матрицы на симметричность
Напишите функцию, которая принимает на вход квадратную матрицу и проверяет,
является ли она симметричной относительно главной диагонали.'''


def is_symmetric(matrix: list) -> bool:
    """is_symmetric - возвращает True, если матрица симметрична относительно главной диагонали,
    и False в противном случае.
    Перебираем строки матрицы и проверяем, равны ли значения в строке с индексом string
    и в столбце с индексом column"""
    for column in range(len(matrix)):
        for string in range(len(matrix)):
            if matrix[column][string] != matrix[string][column]:
                return False
    return True


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [2, 4, 5],
        [3, 5, 6]
    ]
    print(is_symmetric(matrix))