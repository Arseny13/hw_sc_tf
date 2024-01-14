"""
По данным числам n
 и k
 (0≤k≤n)
 вычислите Сkn
. Для решения используйте рекуррентное соотношение Ckn=Ck−1n−1+Ckn−1
.

Решение оформите в виде функции C(n, k).

Входные данные
Вводятся целые числа n и k.

Выходные данные
Выведите ответ на задачу.

Примеры
входные данные
4
2
выходные данные
6
"""


def C(n, k):
    if k == n or k == 0:
        return 1
    if k != 1:
        return C(n-1, k-1) + C(n-1, k)
    else:
        return n


n = int(input())
k = int(input())
print(C(n, k))