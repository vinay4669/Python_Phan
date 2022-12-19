#_func() returns the index of first occurence of uppercse letter in a string
#_or returns -1 if no upper case lette ris present
def func(s):
  if s.islower():
    return -1
  return (1 if s[0].islower() else 0)+(func(s[1:]) if s[0].islower() else 0)
 
s = 'vTUHNm'
print(func(s))#_prints 1

s = 'BYUlBCu'
print(func(s))#_prints 0

s = 'jvyi'
print(func(s))#_prints -1

s = 'algorithM'
print(func(s))#_returns 8