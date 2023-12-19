import math
import random


def guessing_game():
    # Data needs from the user
    lower: int = int(input('Enter the first number: '))
    upper: int = int(input('Enter the last number: '))
    user_answer: int = int(input('Guess the number: '))
    total_num_guess: int = 1

    # Randomly selected answer by computer
    answer: int = random.randint(lower, upper)

    # Minimum number of guesses need to guess the answer
    min_num_guess: int = round(math.log2(upper-lower+1))

    print("Let's start the guessing game. Enjoy the game :)")

    # Logic
    while user_answer != answer:

        if user_answer < answer:
            print('You guessed too low')

        else:
            print('You guessed too high')

        total_num_guess += 1
        user_answer = int(input('Guess the number: '))

    else:
        print(f'You guessed the correct number in {total_num_guess} guesses.')
        print(f'The minimum number of guesses are {min_num_guess}')

guessing_game()


# Python Projects

This repo contains different projects suggested by different websites for python developers to develop and to hone their skills as pyhon programmer. This repo is to help all of those who find hard time solving those problems.

## Suggested by Geeksforgeeks

### Projects for Beginners
1. Number Guessing Game