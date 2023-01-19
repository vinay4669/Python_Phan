n = int(input('Enter a number'))
s = 1
for i in range(2, n):
    s += i if n%i==0 else 0
if n==s:
    print('Perfect No.')
else:
    print('Not a perfect no.')
