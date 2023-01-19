n = int(input('Enter a number : '))
s = 0.0
for i in range(1,n+1):
    f = 1.0
    for j in range(2, i+1):
        f *= j
    s += 1/f
print('Sum of series = ', s)
