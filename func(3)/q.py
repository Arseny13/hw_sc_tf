"""
Напишите функцию phib(n),
которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
В этой задаче нельзя использовать циклы - используйте рекурсию.

phib(1) = phib(2) = 1
phib(n) = phib(n - 1) + phib(n - 2)

Входные данные
Вводится целое число.

Выходные данные
Выведите ответ на задачу.

Примеры
входные данные
6
выходные данные
8
"""


def phib(n):
    if n < 3:
        return 1
    return phib(n - 1) + phib(n - 2)


n = int(input())
print(phib(n))
