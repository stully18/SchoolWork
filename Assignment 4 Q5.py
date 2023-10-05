import random
number = random.randint(1,10)
guess = int(input('Guess a random number between 1 and 10: '))
while number != guess:
    if guess < number:
        print('Too low')
        guess = int(input('Guess again: '))
    elif guess > number:
        print('Too high')
        guess = int(input('Guess again: '))
    else:
        break
print('Congratulations you guessed correctly!!')
