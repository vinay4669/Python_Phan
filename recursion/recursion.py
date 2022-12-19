def fib(a, b, c, n):
    print(b)
    fib(b+c, c, b+c, n-1) if n>1 else 0

n = int(input())
print(f'{n} terms of Fibonacci series:')
fib(0, 0, 1, n)
