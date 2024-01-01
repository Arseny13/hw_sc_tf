# Дана строка, в которой буква h встречается минимум два раза. Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.

# Входные данные
# Вводится строка.

# Выходные данные
# Выведите ответ на задачу.

# Примеры
# входные данные
# In the hole in the ground there lived a hobbit
# выходные данные
# In tobbit

s = input()
first = s.find('h')
last = s.rfind('h')
print(s[:first] + s[last + 1:])
