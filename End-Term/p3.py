def reverse(s, i):
    return s[i-1]+((reverse(s, i-1)) if i>1 else '')

s = input()
if s==reverse(s, len(s)):
    print('Palindrome')
else:
    print('Not Palindrome')