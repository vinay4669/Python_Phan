try:
    l = [0, 1]
    print(l[2])
except ZeroDivisionError:
    print('Error')
finally:
    print('process stop')
print('END')