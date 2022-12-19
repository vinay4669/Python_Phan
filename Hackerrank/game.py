import random
num = random.randint(1, 100)
attempts = 10
while attempts:
    user_num = int(input('guess the numbers 1 to l00') )
    print (f'Attempt left {attempts}')
    attempts-=1
    if user_num==num:
        print('you won! ' , 'with score ', attempts)
        break
    elif user_num<num:
        print("to small")
    else:
        print( "to large")