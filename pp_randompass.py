# Practice Python Excercise 16

import random

def passgen(strength):
    '''
    Takes in the strength of the password as input and returns a 
    randomly generted password consisting of special and alphanumeric 
    characters.
    '''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    ALPHA = alpha.upper()
    num = '0123456789'
    special = '~`!@#$%^&*()-=_+[]|:;",.<>/?'
    population = [alpha, ALPHA, num, special]
    ans = []
    if strength == 's':
        for i in population:
            ans += random.sample(i, 3)
        random.shuffle(ans)
        ans = ''.join(ans)
    else:
        ans = ''.join(random.sample((alpha), 8))
    return ans

def main():
    strength = input('Preferred Password Strength? (s/w): ')
    print('Here is your password:',passgen(strength))

if __name__ == '__main__':
    main()
