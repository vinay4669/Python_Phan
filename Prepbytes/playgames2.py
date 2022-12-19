n = int(input())
a = [2, 3, 4]
for i in range(0, n):
  c = int(input())
  j = 0
  t = 0
  while c>a[j]:
    t += 1
    c -= a[j]
    j += 1
    j %= 2
  if t%2:
    print('Arnab')
  else:
    print('Friend')
