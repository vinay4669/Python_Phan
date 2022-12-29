def distinct(l):
    a = []
    for i in l:
        if i in a:
            return False
        a.append(i)
    else:
        return True


ls = [5, 1, 3, 5, 2, 3, 4, 1]
l = len(ls)
a = []
for i in range(l, -1, -1):
    for j in range(0, i+1):
        if distinct(ls[j:i+1]):
            print(len(ls[j:i+1]))
            exit()
