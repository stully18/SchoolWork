import random

def get_int():
    number = random.randint(1, 10)
    try:
        guess = int(input('Guess a random number between 1 and 10: '))
        while number != guess:
            if guess < number:
                print('Too low')
                guess = int(input('Guess again: '))
            elif guess > number:
                print('Too high')
                guess = int(input('Guess again: '))
        while number == guess:
            print('Congrats you guessed correctly')
            break
        while number == guess:
            decision = input('Press R to restart or Q to quit: \n').capitalize()
            if decision == 'R':
                get_int()
            elif decision == 'Q':
                print('Hope you had fun playing!')
            else:
                print('Please only enter Q or R')
    except ValueError:
        print("Error, that isn't a number!")
        return get_int()

get_int()

decision = input('Press R to restart or Q to quit: \n')
decision = decision.capitalize()
while True:
    if decision == 'R' or 'Q':
        get_int()


