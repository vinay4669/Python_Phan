m, n = list(map(int, input().split()))
l = []
for i in range(m):
    l.append(list(map(int, input().split())))
g = max(m, n)
res = []
for i in range(g//2+1):
    for c in range(i, n-i):
        res.append(l[i][c])
    if len(res)==m*n:
        break
    for r in range(i+1, m-i-1):
        res.append(l[r][n-i-1])
    if len(res)==m*n:
        break
    for c in range(n-i-1, i-1, -1):
        res.append(l[m-i-1][c])
    if len(res)==m*n:
        break
    for r in range(m-i-2, i, -1):
        res.append(l[r][i])
    if len(res)==m*n:
        break
print(res)