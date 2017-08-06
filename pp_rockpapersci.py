

def rps(p1,p2):
    """
    Takes 2 plays as inputs and returns whether which player has won, or 
    whether it is a draw
    """
    rules = {1: ['Rock', 'Scissors'], 2: ['Scissors', 'Paper'], 3: ['Paper', 'Rock']}
    play = [p1,p2]
    if play in rules.values():
        return 'Player 1 wins'
    elif play[::-1] in rules.values():
        return 'Player 2 wins'
    else:
        return 'Draw'
    
def main():  
    again = 'Y' 
    while again == 'Y': 
        p1 = input('Player 1: ')
        p2 = input('Player 2: ')
        print(rps(p1,p2))
        again = input('Want to play?(Y/N) : ')

if __name__ == '__main__':
    main()