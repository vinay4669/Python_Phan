b = [int(('0b'+i), base=2) for i in input().split(',')]
for i in b:
    if i%5==0:
        print(bin(i)[2:]+',')