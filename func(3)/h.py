import sys

d = {}
for line in sys.stdin:
    for word in line.split():
        d[word] = d.get(word, 0) + 1

max_count = max(d.values())
result = [word for word, count in d.items() if count == max_count]
print(min(result))
