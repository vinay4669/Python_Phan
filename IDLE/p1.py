def comb(i, n, s):
    if i==n:
        print(s)
        s = ''
        i = 0
    for i in range(0, n):
        return str(i) + str(comb(i, n-1, s))
        

i = 0
n = 4
s = ''
comb(i, n, s)
