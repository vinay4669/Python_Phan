from decimal import ROUND_05UP


n = int(input())
p = q = 0
r = 1
for i in range(1,n+1):
    print(q)
    p = q+r
    q = r
    r = p