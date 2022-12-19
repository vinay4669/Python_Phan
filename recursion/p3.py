#_prints 16 11 6 1 -4 1 6 11 16
def pattern(n):
  print(n, end = ' ')
  if n>0:
      pattern(n-5)
      print(n, end = ' ')

n = 16
pattern(n)#_16 11 6 1 -4 1 6 11 16