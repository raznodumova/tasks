"""Задача 1: Проверка матрицы на симметричность
Напишите функцию, которая принимает на вход квадратную матрицу и проверяет,
является ли она симметричной относительно главной диагонали."""


def is_symmetric(matrix: list[list[int]]) -> bool:
    """is_symmetric - возвращает True,
    если матрица симметрична относительно главной диагонали,
    и False в противном случае.
    Перебираем строки матрицы и проверяем,
    равны ли значения в строке с индексом row
    и в столбце с индексом col"""
    for row in range(len(matrix)):
        for col in range(row, len(matrix)):
            if matrix[col][row] != matrix[row][col]:
                return False
    return True


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [2, 4, 5],
        [3, 5, 6]
    ]
    print(is_symmetric(matrix))
