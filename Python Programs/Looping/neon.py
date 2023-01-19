n = int(input('Enter a number'))
s = n ** 2
a = 0
while s>0:
    a += s % 10
    s //= 10
if a==n:
    print('Neon No.')
else:
    print('Not a Neon no.')
