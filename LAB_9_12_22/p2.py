n = int(input('Enter the size of matrix:'))
l = [[0]*n for i in range(0, n)]
x = 1
s = ''
st = ''
for r in range(0, n):
    for c in range(0, n):
        l[r][c] = x
        x += 1
t = 0 if n%2==0 else 1
for i in range(0, n):
    a = 0
    b = i
    for j in range(0, i+1):
        st += str(l[a][b])+' '
        a += 1
        b -= 1
    tmp = st.split()
    if i%2==0:
        tmp.reverse()
    s += '  '.join(tmp) + '  '
    st = ''
for i in range(0, n-1):
    a = i+1
    b = n-1
    for j in range(0, n-i-1):
        st += str(l[a][b])+' '
        a += 1
        b -= 1
    tmp = st.split()
    if i%2==t:
        tmp.reverse()
    s += '  '.join(tmp) + '  '
    st = ''
print(s)