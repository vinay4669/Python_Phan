b = 51
while b>0:
    print('Input no. of balls you want to pick(less than 5)')
    n = int(input())
    if n<1 or n>4:
        print('INVALID INPUT')
    else:
        b -= n
print('You lose!')