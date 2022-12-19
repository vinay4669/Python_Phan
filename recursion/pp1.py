a = 1
b = 2
c = 3
d = 4
l = [f'{l}{k}{j}{i}' for l in range(1, d+1) for k in range(1, c+1) for j in range(1, b+1) for i in range(1, a+1)]
print(len(l))
for i in l:
    print(i)

'''
def comb(n, s):
    global g
    for i in range(1, n+1):
        comb(n-1, s+str(i))
        print(s)

g = 4
n = 4
ind = 1
s = ''
comb(n, s)
'''

'''
def comb(c, n, s):
    for i in range(1, n+1):
        if c<n:
            comb(c+1, n, s+str(i))
    if c==n:
        c = 0
        print(s)
        s = ''

n = 10
c = 0
s = ''
comb(c, n, s)
'''

'''
def unique(n):
    j = 1
    for i in n:
        if i in n[j:]:
            return False
        j += 1
    return True

def comb(c, n, s):
    global a
    for i in range(1, n+1):
        if c<n:
            comb(c+1, n, s+str(i))
    if c==n:
        c = 0
        if unique(s):
            print(s)
            a.append(s)
        s = ''

a = []
n = int(input())
c = 0
s = ''
comb(c, n, s)
print(a)
'''