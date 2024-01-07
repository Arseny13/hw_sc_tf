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
