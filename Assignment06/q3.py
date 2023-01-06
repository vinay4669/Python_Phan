f = open("sample.txt", 'r')
l = f.readlines()
r = []
for i in l:
    if 'a' not in i:
        r.append(i)
f.close()
f = open("sample2.txt", 'w')
for i in r:
    f.write(i)
f.close()