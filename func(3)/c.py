s = input()
st = set()
result = ''
for c in s:
    if c not in st:
        st.add(c)
        result += c
print(result)
