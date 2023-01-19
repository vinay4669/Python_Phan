def fib(n, p, q, r):
    return q if n<2 else fib(n-1, q, r, q+r)

n = int(input())
for i in range(1,n+1):
    print(fib(i,0,0,1))