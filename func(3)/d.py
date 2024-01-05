s1 = input()
s2 = input()
st1 = set(s1)
st2 = set(s2)
result = sorted(list(st1 & st2))
if result:
    print(*result, sep='')
else:
    print('NO')
