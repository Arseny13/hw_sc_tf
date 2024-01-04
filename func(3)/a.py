s = input()
s1 = set('.,;:!?')
k = 0
for c in s:
    if c in s1:
        k += 1
print(k)
