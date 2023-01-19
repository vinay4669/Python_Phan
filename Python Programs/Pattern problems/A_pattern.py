n = int(input())
x = n%2==0
for i in range(n):
    if i==n//2:
        print((n//2-x)*' ' + (n+x)*'*')
    else:
        print((n-i-1)*' ' + '*' + ' '*(i*2-1) + ('*' if i else ''))
