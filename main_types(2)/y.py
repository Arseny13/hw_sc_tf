# Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы имевшие индекс не менее k вправо.

# Поскольку при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет добавить новый элемент, используя метод append().

# Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.

# Входные данные
# Вводится список чисел. Все числа списка находятся на одной строке. В следующей строке вводятся два целых числа.

# Выходные данные
# Выведите ответ на задачу.

# Примеры
# входные данные
# 7 6 5 4 3 2 1
# 2 0
# выходные данные
# 7 6 0 5 4 3 2 1

s = [int(s) for s in input().split()]
k, C = [int(s) for s in input().split()]
s.append(0)
for i in range(len(s) - 1, k, -1):
    s[i] = s[i - 1]
s[k] = C
print(*s)
