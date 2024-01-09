"""
Дан текст (строк может быть много).
Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите то,
которое меньше в лексикографическом порядке.

Входные данные
Вводится текст.

Выходные данные
Выведите ответ на задачу.

Примеры
входные данные
apple orange banana banana orange
выходные данные
banana
"""

import sys

d = {}
for line in sys.stdin:
    for word in line.split():
        d[word] = d.get(word, 0) + 1

max_count = max(d.values())
result = [word for word, count in d.items() if count == max_count]
print(min(result))
