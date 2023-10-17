num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter a second number: '))
if num1 == 0:
    print(f'The GCD of {num1} and {num2} is {num2}')
elif num2 == 0:
    print(f'The GCD of {num2} and {num1} is {num1}')
#This conditional switched the value of num1 and num2 if num1 is less than num2
if num1<num2:
    temp = num1
    num1 = num2
    num2 = temp
#I used exception handling to prevent a ZeroDivisionError
try:
    def euc():
        r1 = num1 % num2
        if r1 == 0:
            print(f'The GCD of {num1} and {num2} is {num2}')
        while r1 != 0:
            r2 = num2 % r1
            if r2 != 0:
                r3 = r1 % r2
                if r3 != 0:
                    r4 = r2 % r3
                    if r4 != 0:
                        r5 = r3 % r4
                        if r5 != 0:
                            r6 = r4 % r5
                            if r6 !=0:
                                r7 = r5 % r6
                                if r7 != 0:
                                    r8 = r6 % r7
                                    if r8 != 0:
                                        r9 = r7 % r8
                                        if r9 != 0:
                                            r10 = r8 % r9
                                            if r10 != 0:
                                                r11 = r9 % r10
                                                if r11 != 0:
                                                    r12 = r10 % r11
            if r2 == 0:
                print(f'The GCD of {num2} and {num1} is {r1}')
            elif r3 == 0:
                print(f'The GCD of {num2} and {num1} is {r2}')
            elif r4 == 0:
                print(f'The GCD of {num2} and {num1} is {r3}')
            elif r5 == 0:
                print(f'The GCD of {num2} and {num1} is {r4}')
            elif r6 == 0:
                print(f'The GCD of {num2} and {num1} is {r5}')
            elif r7 == 0:
                print(f'The GCD of {num2} and {num1} is {r6}')
            elif r8 == 0:
                print(f'The GCD of {num2} and {num1} is {r7}')
            elif r9 == 0:
                print(f'The GCD of {num2} and {num1} is {r8}')
            elif r10 == 0:
                print(f'The GCD of {num2} and {num1} is {r9}')
            elif r11 == 0:
                print(f'The GCD of {num2} and {num1} is {r10}')
            break

except ZeroDivisionError:
    print('')
euc()
