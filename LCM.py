try:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def euc():
        try:
            num1 = int(input('Please enter a number: ')) 
            num2 = int(input('Please enter a second number: ')) 
            gcd_result = gcd(max(num1, num2), min(num1, num2))
            LCM = (num1*num2)/gcd_result 
            if num1 == 0:
                print(f'The GCD of {num1} and {num2} is {num2}')
            elif num2 == 0:
                print(f'The GCD of {num2} and {num1} is {num1}')
            else:
                gcd_result = gcd(max(num1, num2), min(num1, num2))
                print(f'The GCD of {num1} and {num2} is {gcd_result} and the LCM is {LCM}')

        except ValueError:
            print('Please only enter numbers. ')
            return euc()
    euc()
except ValueError:
    print('Please only enter numbers. ')
    euc()
