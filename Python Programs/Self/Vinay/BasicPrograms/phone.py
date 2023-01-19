a = [1]*500
for i in range(1,501):
    for j in range(i,501):
        if j%i==0:
            a[j-1] = 0 if a[j-1] else 1
print('Roll no. of students whose phone is off')
for i in range(1,501):
    if not a[i-1]:
        print(i)