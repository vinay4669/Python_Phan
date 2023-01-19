# it just flattens a dictionary

def flatten(d, res = {}, x = ''):
    for i, j in d.items():
        if type(j)==dict:
            flatten(j, res, x+i+'.')
        else:
            res[x+i] = j
    return res

# d1 = {'k1':{'foo': {'a': 5, 'bar': {'baz': 8 }}, 'key': 3}}
d1 = {'abc':123, 'hgf':{'gh':432, 'yu':433}, 'gfd':902, 'xzxzxz':{"432":{'0b0b0b':231}, "43234":1321}}
print(flatten(d1))