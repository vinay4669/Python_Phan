s = input('Input a string : ')
ss = input('Enter the substring you want to search : ')
if ss in s:
    ind = s.find(ss)
    print('Yes, {} is present in {} and it\'s index is {}'.format(ss, s, ind))
else:
    print('{} is not present in {}'.format(ss, s))
    
