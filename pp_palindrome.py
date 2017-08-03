'''
Practice Python Excercise 6 
'''

def palindrome(n):
    '''
    Takes a string as input and prints out 'Yes' or 'No' based on
    whether it is a string or not
    '''
    n1 = n[::-1]
    if n[:(len(n)//2)] == n1[:(len(n)//2)]:
        return 'Yes'
    else:
        return 'No'

def main():
    n = input('Enter the string: ')
    palindrome(n)

if __name__ == '__main__':
    main()