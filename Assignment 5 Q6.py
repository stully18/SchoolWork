
def palindrome():
    try:
        number = (input('Please enter a number: '))
        reverse_number = number[::-1]

        if number.isnumeric() == False:
            print('Please only enter numbers:')
            return palindrome()
        elif number == reverse_number:
            print(f'{number} is a palindrome!')
            return palindrome()
        else:
            print(f'{number} is not a palindrome')
            return palindrome()
    except ValueError:
        print('Please only enter numbers.')
        return palindrome()
palindrome()
