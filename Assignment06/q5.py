f = open("sample4.bin", 'rb')
lines = f.readlines()
f.close()
rn = input('Enter roll number : ')
m = input('Enter new marks : ')
f2 = open("sample4.bin", 'wb')
f3 = open("sample4.bin", 'ab')
f2.write(b'')
f2.close()
for i in lines:
    st = f'{i}'
    st = (st[2:len(st)-5]).split()
    if rn==st[1]:
        st[2] = m
    st = ' '.join(st)
    r = bytes(st+'\n', 'utf-8')
    f3.write(r)
f3.close()
