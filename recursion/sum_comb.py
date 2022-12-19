def sum_comb(s, n, c):
    for i in range(1, n):
        if s<n:
            sum_comb(s+i, n, f'{c}+{i}')
        elif s>n:
            sum_comb(s-i, n, c[:-1])
        else:
            print(c)


n = 5
sum_comb(0, n, '')