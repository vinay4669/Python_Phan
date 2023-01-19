n = int(input("Enter a 3 digit no."))
temp = n
rev = n%10
n //= 10
rev = rev*10 + (n%10)
n //= 10
rev = rev*10 + (n%10)
if temp==rev:
    print('Palindrome number')
else:
    print('Not a palindrome number')