n = input()
l = len(n)
st = ''
while 1:
    li = list(map(str, n))
    for i in range(0,l):
        for j in range(0,l-1):
            if li[j]>li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    a = d = ''
    a = int(a.join(li))
    li.reverse()
    d = int(d.join(li))
    n = str(d-a)
    if n not in st:
        st += n + ' '
    else:
        print(n)
        break