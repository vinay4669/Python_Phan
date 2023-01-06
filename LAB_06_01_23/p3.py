import random
l = [chr(i) for i in list(range(65, 91)) + list(range(97, 123))]
print(''.join(random.sample(l, 5)))