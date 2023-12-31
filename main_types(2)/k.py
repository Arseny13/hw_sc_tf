# Исполнитель “Раздвоитель” преобразует натуральные числа. У него есть две команды: “Вычесть 1” и “Разделить на 2”, первая команда уменьшает число на 1, вторая команда уменьшает число в два раза, если оно чётное, иначе происходит ошибка.

# Входные данные
# Дано два натуральных числа A и B (A>B).

# Выходные данные
# Напишите алгоритм для Развоителя, который преобразует число A в число B и при этом содержит минимальное число команд. Команды алгоритма нужно выводить по одной в строке, первая команда обозначается, как -1, вторая команда как :2.

# Примеры
# входные данные
# 179
# 20
# выходные данные
# -1
# :2
# -1
# :2
# :2
# -1
# -1

A = int(input())
B = int(input())
while A != B:
    if (A // 2 >= B) and (A % 2 == 0):
        print(':2')
        A //= 2
    else:
        print('-1')
        A -= 1
