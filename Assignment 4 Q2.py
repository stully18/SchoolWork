num1 = float(input('Enter a number: '))
num2 = float(input('Enter a second number: '))
ans = (num1-num2)
if ans.is_integer() ==True:
    print('The difference of '+str(num1)+' and '+str(num2)+' is an integer')
else:
    print('The difference of '+str(num1)+' and '+str(num2)+' is not an integer ')



