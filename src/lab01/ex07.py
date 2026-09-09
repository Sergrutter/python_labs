s = input()

s_otv = ''
ind_a = 0
ind_b = 0

for c in s:
    if c.lower() != c:
        s_otv += c
        ind_a = s.index(c)
        break

for c in s:
    if c in '0123456789':
        ind_b = s.index(c) + 1
        break

for i in range(ind_b, len(s), ind_b - ind_a):
    s_otv += s[i]

print(s_otv)