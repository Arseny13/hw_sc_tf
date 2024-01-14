"""
Дана последовательность целых чисел, заканчивающаяся числом 0.
Выведите эту последовательность в обратном порядке.

При решении этой задачи нельзя пользоваться массивами
и прочими динамическими структурами данных. Рекурсия вам поможет.

Входные данные
Вводится последовательность целых чисел, оканчивающаяся числом 0.

Выходные данные
Выведите ответ на задачу.

Примеры
входные данные
1
2
3
0
выходные данные
0
3
2
1
"""


def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)


reverse()