import random
from collections import Counter
someWords = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

words = someWords.split(' ')

word = random.choice(words)

def hangman():
    print('Guess the word and enjoy the game.')
    print('HINT: Word is name of a fruit. ')


    for i in word:
        print('_', end='')
    print()

    turns = len(word) + 2
    guessed_letter = ''
    playing = True
    correct = 0
    flag = 0

    while (turns != 0) and (flag == 0):
        print()
        turns -= 1

        guess = input('Guess the letter: ')

        if not guess.isalpha():
            print('Enter a letter')
            continue
        elif len(guess) > 1:
            print('Enter only one letter')
            continue
        elif guess in guessed_letter:
            print('You have guessed this letter. Guess another letter.')

        if guess in word:
            num_time = word.count(guess)

            for _ in range(num_time):
                guessed_letter += guess

        for char in word:
            if char in guessed_letter and (Counter(guessed_letter) != Counter(word)):
                print(char, end='')
                # print()
                correct += 1

            elif Counter(guessed_letter) == Counter(word):
                print(f'Your guessed word is {guessed_letter}')
                print(word)

                flag = 1
                print('You Won')
                break

            else:
                print('_', end='')
        #
        if turns == 0 and (Counter(guessed_letter) != Counter(word)):
            print('You have lost. Try Again')
            print(f'The word is {word}')

# print(word)
hangman()
