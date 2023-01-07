f = open("lab1.txt", 'r')
l = ((f.readlines()))
f.close()
f = open("lab3.txt", 'w')
c = 0
for i in l:
    for j in i.split():
        if c%2==0:
            f.write(j+' ')
        c += 1
f.close()