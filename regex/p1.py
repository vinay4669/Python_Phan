import re

str = 'VnbVV 12'
patt = re.compile(r'(?=.*[a-z])(?=.*[A-Z])')
matches = patt.finditer(str)
for match in matches:
    print(match)