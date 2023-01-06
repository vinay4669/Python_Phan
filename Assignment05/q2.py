import flatdict

def flatten(d):
    print(flatdict.FlatDict(d, delimiter='.'))

d = eval(input())
flatten(d)