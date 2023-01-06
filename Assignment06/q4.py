f = open("sample3.bin", 'rb')
lines = f.readlines()
rn = input()
for i in lines:
    st = f'{i}'
    if rn in st:
        print(st.split()[0][2:])
        break
else:
    print('Roll no. not found')