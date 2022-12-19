n = int(input())
x = 2*n-1
z = n
l = [[0]*x for i in range(0, x)]
for i in range(0, x//2):
    for c in range(i, x-i):
        l[i][c] = z
    for r in range(i+1, x-i-1):
        l[r][x-i-1] = z
    for c in range(x-i-1, i-1, -1):
        l[x-i-1][c] = z
    for r in range(x-i-2, i, -1):
        l[r][i] = z
    z -= 1
l[x//2][x//2] = 1
for r in range(0, x):
    for c in range(0, x):
        print(l[r][c], end = '\t')
    print()