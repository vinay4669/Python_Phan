from re import L


n = int(input())
a = [[0]*n]*n
l = 1
for i in range(0, n//2):
    for b in range(i, n-i):
        a[i][b] = l
        l += 1
    for c in range(i+1, n-i-1):
        a[c][n-i-1] = l
        l += 1
    for d in range(n-i-1, i-1, -1):
        a[n-i-1][d] = l
        l += 1
    for e in range(n-i-2, i, -1):
        a[e][i] = l
        l += 1
for x in range(n):
    for y in range(n):
        print('\t', a[x][y], end = '')
    print()