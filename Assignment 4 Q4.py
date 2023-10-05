a = int(input('Enter a value of 0 or 1: '))
b = int(input('Enter a value of 0 or 1: '))

if a==0 and b==0:
    print('The value of Q is 0')
elif a==0 and b==1:
    print('The value of Q is 1')
elif a==1 and b==0:
    print('The value of Q is 1')
elif a==1 and b==1:
    print('The value of Q is 0')
else:
    print('Please only input 0s and 1s')