f = open("lab1.txt", 'r')
l = f.read()
nv = 0
v = 'AEIOUaeiou'
for i in l:
    if i in v:
        nv += 1
print('No. of vowels :', nv)