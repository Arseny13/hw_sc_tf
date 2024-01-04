s = input()
s1 = set()
s2 = set()
for c in s:
    if ('0' <= c <= '9') and c not in s1:
        s1.add(c)
    elif c in s1:
        s2.add(c)
if len(s2) > 0:
    s2 = sorted(list(s2))
    print(*s2, sep='')
else:
    print('NO')
