#Practice Python Excercise 20

def binary(sorted_l,item):
    '''Given a list of sorted elements, it searches for 
    given one''' 
    low = 0
    high = len(sorted_l)-1
 
    while True:
        mid = (high + low)//2
        guess = sorted_l[mid]
        if guess == item:
            print(f'Item found!')
            break
        elif guess < item:
            low = mid+1
        else:
            high = mid
    return mid
        

def main():
    l = input('Enter a list of numbers: ')
    a = [int(x) for x in l.split()]
    s_item = int(input('Which number do you want to search?: ')) 
    sorted_l = sorted(a)
    binary(sorted_l, s_item)

if __name__ == '__main__':
    main()
