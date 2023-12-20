import random

def guess_word():
    name: str = input('Enter your name: ')

    print(f'Good Luck {name}')

    words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

    word = random.choice(words)

    turns = len(word) + 5

    print('Guess the characters')

    guesses = ''

    while turns > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char, end='')

            else:
                print('_')
                failed += 1

        if failed == 0:
            print('\nYou win 😊')
            break

        print()
        guess = input('Guess your character: ')

        guesses += guess

        if guess not in word:
            turns -= 1

            print('Wrong ☹️')

            print(f'You have {turns} left.')


guess_word()
