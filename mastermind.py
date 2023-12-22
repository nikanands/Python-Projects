import random

def mastermind():
    num = str(random.randint(1000, 10000))
    print(num)
    guess = str(input('Guess the 4 digit number: '))

    count = 0

    if (num == guess):
        print(f'You have guessed the number in 1 try. The number is {num}')

    else:
        while (guess != num):
            count += 1
            # input('Guess')
            correct_digit = ['X']*4
            correct_digit_count = 0

            for i in range(0,4):
                if num[i] == guess[i]:
                    correct_digit_count += 1
                    correct_digit[i] = num[i]
                else:
                    continue

            print(f'Not the correct number but you guessed {correct_digit_count} digit correct')

            guess = str(input('Enter your new guess: '))

            if correct_digit_count == 0:
                print('You have not guess any digit correct. Please guess another number')
                guess = str(input('Enter your new guess: '))

        if num == guess:
            count += 1
            print('You are a mastermind.')
            # print(correctDigit)
            # print(num, guess, count, correctDigit)




mastermind()