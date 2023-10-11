def activity9():
    try:
        days_after = int(input('How many days after Wednesday has it been?\n'))
        days_after = days_after % 7
        if days_after==0:
            print('It is Wednesday!')
            return activity9()
        elif days_after == 1:
            print('It is Thursday!')
            return activity9()
        elif days_after == 2:
            print('Today is Friday!')
            return activity9()
        elif days_after == 3:
            print('Today is Saturday!')
            return activity9()
        elif days_after == 4:
            print('Today is Sunday!')
            return activity9()
        elif days_after == 5:
            print('Today is Monday!')
            return activity9()
        elif days_after == 6:
            print('Today is Tuesday!')
            return activity9()
    except ValueError:
        print('Please only enter numbers:')
        return activity9()
activity9()