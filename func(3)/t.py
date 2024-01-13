"""
Для быстрого вычисления наибольшего общего делителя двух чисел
используют алгоритм Евклида. Он построен на следующем соотношении:
НОД(a,b)=НОД(b,amodb).

Реализуйте рекурсивный алгоритм Евклида в виде функции gcd(a, b).

Входные данные
Вводится два целых числа.

Выходные данные
Выведите ответ на задачу.

Примеры
входные данные
12
14
выходные данные
2
входные данные
256
48
выходные данные
16
"""


def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return b


a = int(input())
b = int(input())
print(gcd(a, b))
