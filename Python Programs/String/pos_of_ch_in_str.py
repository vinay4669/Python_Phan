s = input('Enter a string : ')
c = input('Enter an element you want index for : ')
'''
start = 0
for i in range(s.count(c)):
    i = s.index(c, start)
    print(i)
    start = i + 1
'''
x = 0
while c in s:
    i = s.find(c)
    print(x + i)
    x = i + 1
    s = s[x:]
