from itertools import groupby

s = '1222311'
for i, j in groupby(s):
    print((len(list(j)), int(i)), end = ' ')