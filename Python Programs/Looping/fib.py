n = int(input())
a = b = 0
c = 1
for i in range(0, n):
    print(b)
    a = b + c
    b = c
    c = a
