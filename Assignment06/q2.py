f = open("sample.txt", 'r')
l = f.readlines()
v = c = uc = lc= 0
ucl = [chr(i) for i in range(65, 91)]
lcl = [chr(i) for i in range(97, 123)]
vl = 'aeiouAEIOU'
for i in l:
    for j in ''.join(i.split()):
        if j in ucl:
            uc += 1
        else:
            lc += 1
        if j in vl:
            v += 1
        else:
            c += 1
print('No. of vowels', v)
print('No. of consonants', c)
print('No. of uppercase letters', uc)
print('No. of lowercase letters', lc)
f.close()