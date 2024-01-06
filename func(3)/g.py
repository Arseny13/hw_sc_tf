N = int(input())
d = {}
for i in range(N):
    word, word2 = input().split()
    d[word] = word2
    d[word2] = word
str = input()
print(d[str])
