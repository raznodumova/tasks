'''Задача 1: Проверка матрицы на симметричность
Напишите функцию, которая принимает на вход квадратную матрицу и проверяет,
является ли она симметричной относительно главной диагонали.'''


def is_symmetric(matrix: list) -> bool:
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
            else:
                return True


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [2, 4, 5],
        [3, 5, 6]
    ]
    print(is_symmetric(matrix))