b = [int(('0b'+i), base = 2) for i in input().split(',')]
res = []
for i in b:
    if i%5==0:
        res.append(bin(i)[2:])
print(','.join(res))