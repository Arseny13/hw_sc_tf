# Выведите все точные квадраты натуральных чисел, не превосходящие данного числа N.

# Входные данные
# Задано единственное целое число N

# Выходные данные
# Необходимо вывести  все точные квадраты натуральных чисел, не превосходящие данного числа N.

# Примеры
# входные данные
# 15
# выходные данные
# 1
# 4
# 9

n = int(input())
i = 1
while True:
    if i*i <= n:
        print(i*i)
        i += 1
    else:
        break
