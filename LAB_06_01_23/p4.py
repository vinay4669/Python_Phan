import random
uc = [chr(i) for i in list(range(65, 91))]
lc = [chr(i) for i in list(range(97, 123))]
dg = list(range(0, 10))
sc = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ':', '"', '\'', ';', '<', ',', '>', '.', '/', '?', '\\', '|']
lo = random.sample(uc, 2) + [f'{random.choice(dg)}'] + [f'{random.choice(sc)}'] + random.sample(lc, 6)
print(''.join(lo))