
'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they 
guessed too low, too high, or exactly right.

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken,
and when the game ends, print this out.
'''
import random

def main():
    again = 'y'
    count = 0
    while again == 'y':
        count += 1
        guess = int(input('Guess the number: '))
        randgen = ((random.random()*10)//1)
        if guess == randgen:
            print("Right!")
        elif guess < randgen:
            print('Too Low!')
        else:
            print("Too High!")
        again = input('Guess Again? (y/n): ')
        if again == 'n':
            print(f'You guessed {count} times')

if __name__ == '__main__':
    main()