convert = lambda f: (f-32)/1.8
f = float(input('Enter temperature in fahrenheit'))
print(f'Temperature in celsius : {convert(f)}')