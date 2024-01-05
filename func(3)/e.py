s1 = input().lower()
s2 = input().lower()
st1 = set()
st2 = set()
for c in s1:
    if 'a' <= c <= 'z':
        st1.add(c)
for c in s2:
    if 'a' <= c <= 'z':
        st2.add(c)
st3 = st1 | st2
result = list(map(chr, range(97, 123)))
if not st3 or st3 == set(result):
    print(0)
else:
    for c in result:
        if c not in st3:
            print(c.upper(), end='')
