d = {}
for i in range(int(input())):
    country, *city = input().split()
    for c in city:
        d[c] = country
for i in range(int(input())):
    s = input()
    print(d[s])
