from math import *
n = int(input())
for i in range(0, n):
  n = int(input())
  while n>1:
    print(n)
    n = int(pow(n, (1.5 if n%2 else 0.5)))