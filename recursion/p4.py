#_function to reverse a number
def reverse(n, l):
  return (n%10)*(10 ** (l-1)) + (reverse(n//10, l-1) if n>9 else 0)
  
n = 7735.8
l = len(str(n))
print(reverse(n, l))#5377