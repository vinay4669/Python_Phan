def asm(a, b, n, w):
    if a==n:
        return w
    elif a<n:
        asm(a+b, b, n, w-1)
    else:
        asm(1, 2, n, w)


print(asm(1, 2, 12, 1))
print(asm(1, 2, 13, 1))
print(asm(1, 2, 13, 2))
print(asm(1, 2, 13, 3))
print(asm(1, 2, 13, 4))