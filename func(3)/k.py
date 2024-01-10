"""
Для каждого элемента дерева определите число всех его потомков
(не считая его самого).

Входные данные
Формат входных данных совпадает с задачей W.

Выходные данные
Формат выходных данных совпадает с задачей W.
Выведите список всех элементов в лексикографическом порядке,
для каждого элемента выводите количество всех его потомков.

Примечание
Решение должно иметь сложность O(N),
не считая сложности обращения к элементам словаря и сортировки результата.

Примеры
входные данные
9
Alexei Peter_I
Anna Peter_I
Elizabeth Peter_I
Peter_II Alexei
Peter_III Anna
Paul_I Peter_III
Alexander_I Paul_I
Nicholaus_I Paul_I
выходные данные
Alexander_I 0
Alexei 1
Anna 4
Elizabeth 0
Nicholaus_I 0
Paul_I 2
Peter_I 8
Peter_II 0
Peter_III 3
"""

from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


def count_descendants(name, tree, descendants):
    if descendants[name] != -1:
        return
    cntr = len(tree[name])
    for child in tree[name]:
        if descendants[child] == -1:
            count_descendants(child, tree, descendants)
        cntr += descendants[child]
    descendants[name] = cntr


n = int(input())
tree = defaultdict(list)
descendants = {}
for _ in range(n - 1):
    child, parent = input().split()
    tree[parent].append(child)
    if child not in descendants:
        descendants[child] = -1
    if parent not in descendants:
        descendants[parent] = -1

for name in sorted(descendants.keys()):
    count_descendants(name, tree, descendants)
    print(name, descendants[name])
