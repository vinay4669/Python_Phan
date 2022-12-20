def sum_comb(s, n, c):
    global a
    for i in range(1, n):
        if s<n:
            sum_comb(s+i, n, f'{c}+{i}')
        elif s>n:
            return 0
        else:
            c = c.strip('+')
            a.append(c) if c not in a else 1

a = []
n = int(input())
sum_comb(0, n, '')
for i in a:
    print(i)