import random

def unique(n):
    j = 1
    '''for i in n:
        if i in n[j:]:
            return False
        j += 1'''
    return True

def comb(c, n, s):
    global a
    for i in range(1, n+1):
        #remove f'{i}' not in s for getting combinations with repetitions
        #if c<n and f'{i}' not in s:
        #    comb(c+1, n, s+str(i))
        if c<n:
            comb(c+1, n, s+str(i))
    if c==n:
        c = 0
        if unique(s):
            #print(s)
            a.append(s)
        #print(s)
        s = ''

a = []
n = int(input())
c = 0
s = ''
comb(c, n, s)
print(a)
#print(len(a))
#print(random.choice(a))