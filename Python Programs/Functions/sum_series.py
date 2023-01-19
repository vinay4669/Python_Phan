def sum_series(n):
    sum = 0
    for i in range(1, n+1):
        sum += 1/factorial(i)
    return sum

def factorial(n):
    return n*((factorial(n-1)) if n>1 else 1)

n = int(input('Enter the limit: '))
print('Sum of series = ', sum_series(n))
