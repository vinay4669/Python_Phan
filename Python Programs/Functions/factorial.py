def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

n = int(input('Enter a number:'))
print('Factorial of {} is {}'.format(n, factorial(n)))
