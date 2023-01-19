n = int(input("Enter a 3 digit no."))
rev = n%10
n //= 10
rev = rev*10 + (n%10)
n //= 10
rev = rev*10 + (n%10)
print('Reverse = ', rev)