# User is able to guess numbers against a number set by your program //
# If user enters anything other than number, user should be told //
# There are 3 levels, easy, medium and hard
# At easy, Users get a chance to guess the number between 1 - 10, and the user gets 6 guesses//
#
# Medium, the users is required to guess the number between 1 - 20, and the user gets 4 guesses//
#
# Hard, users are required to guess between 1 - 50, and they only get 3 guesses//
#
# User should be able to set the level they want to play//
#
# Users should see how many guesses they have left after each guess//
#
# If user guesses right, user should be told "You got it right!"//
# If the user guesses wrong, user should be told "That was wrong"//
# If users uses all available guessing power and still unable to guess right, user should be told "Game over!"//


import random

game_instructions = ('There are three levels in this game: Easy(E), Medium (M) and Hard(H)')
print(game_instructions)

set_level = input('Which level would you like to play? (Enter E for easy, M for medium and H for hard) ').lower()

start = True
# Easy
while start:
    if set_level == "e":
        print('The number is between 1-10. You have six(6) guesses')
        secret_number = random.randint(1, 10)
        # print(secret_number)   # for program test
        guess_limit = 6
        while guess_limit:
            try:
                guess = int(input('Guess: '))
                if guess == secret_number:
                    print('You got it right!')
                    start = False
                    break
            except ValueError:
                print('Invalid input! Enter a number')

            else:
                while guess_limit >= 1:
                    guess_limit = guess_limit - 1
                    if guess_limit >= 2:
                        print(f'That was wrong! You have {guess_limit} guesses left')
                    elif guess_limit == 1:
                        print(f'That was wrong! You have {guess_limit} guess left')
                    if guess_limit == 0:
                        print('Game Over!')
                        start = False
                    break


    # Medium
    elif set_level == "m".lower():
        print('The number is between 1-20. You have four (4) guesses')
        secret_number = random.randint(1, 20)
        # print(secret_number)  # For program test
        guess_limit = 4
        while guess_limit:
            try:
                guess = int(input('Guess: '))
                if guess == secret_number:
                    print('You got it right!')
                    start = False
                    break
            except ValueError:
                print('Invalid input! Enter a number')

            else:
                while guess_limit >= 1:
                    guess_limit = guess_limit - 1
                    if guess_limit >= 2:
                        print(f'That was wrong! You have {guess_limit} guesses left')
                    elif guess_limit == 1:
                        print(f'That was wrong! You have {guess_limit} guess left')
                    if guess_limit == 0:
                        print('Game Over!')
                        start = False
                    break


    # Hard
    elif set_level == "h".lower():
        print('The number is between 1-50. You have three (3) guesses')
        secret_number = random.randint(1, 50)
        # print(secret_number)  # for program test
        guess_limit = 3
        while guess_limit:
            try:
                guess = int(input('Guess: '))
                if guess == secret_number:
                    print('You got it right!')
                    start = False
                    break
            except ValueError:
                print('Invalid input! Enter a number')

            else:
                while guess_limit >= 1:
                    guess_limit = guess_limit - 1
                    if guess_limit >= 2:
                        print(f'That was wrong! You have {guess_limit} guesses left')
                    elif guess_limit == 1:
                        print(f'That was wrong! You have {guess_limit} guess left')
                    if guess_limit == 0:
                        print('Game Over!')
                        start = False
                    break

    else:
        print('Invalid input! (Enter E for easy, M for medium and H for hard)')
        set_level = input(
            'Which level would you like to play? (Enter E for easy, M for medium and H for hard) ').lower()
        start = True


