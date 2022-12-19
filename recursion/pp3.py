# work in progress
# idk what i'm doing

a = []
def main():
    global a
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    comb(0, [x, y, z], [], n)
    print(a)
    

def comb(c, n, l, s):
    global a
    for i in range(0, n[c]):
        if c<n[c]-1:
            comb(c+1, n, l.append(i), s)
    if c==n[c]-1:
        if sum(l)!=s:
            a.append(l)
        c = 0
        l = []
        
main()