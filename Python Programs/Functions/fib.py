def fib(n):
    a = 0
    b = 0
    c = 1
    for i in range(0, n):
        print(b, end = ', ')
        a = b + c
        b = c
        c = a

n = int(input('Enter a number : '))
fib(n)
