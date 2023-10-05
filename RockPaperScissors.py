import random
choices = ['Rock', 'Paper', 'Scissors']
computer_choice = random.choice(choices)
person_choice = input('Rock, Paper, or Scissors \n')
person_choice = person_choice.capitalize()
print(f"You chose {person_choice}, computer chose {computer_choice}.")
while person_choice == 'Rock' or 'Paper' or 'Scissors':
    if computer_choice == person_choice:
        print(f'You guys both chose {person_choice}, it is a tie')
    elif computer_choice == 'Rock' and person_choice == 'Paper':
        print('You Won!')
    elif computer_choice == 'Rock' and person_choice == 'Scissors':
        print('You Lost :(')
    elif computer_choice == 'Scissors' and person_choice == 'Paper':
        print('You Lost :(')
    elif computer_choice == 'Scissors' and person_choice == 'Rock':
        print('You Won!')
    elif computer_choice == 'Paper' and person_choice == 'Rock':
        print('You Lost :(')
    elif computer_choice == 'Paper' and person_choice == 'Scissors':
        print('You Won!')
    break
#Maximous Nabil Masih is a devine feminine