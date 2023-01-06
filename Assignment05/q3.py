n = int(input())
l = list(map(int, input().split()))
m = l[0]
for i in l:
    if l.count(m) < l.count(i):
        m = i
print(l.count(m))