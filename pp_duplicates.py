#Practice Python Excercise 14

def duplicates(l):
    '''Given a list, it returns another minus all the duplicates using
    a for loop.'''
    l1 = []
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1

def set_way(l):
    '''Given a list, it returns another minus all the duplicates using 
    sets.'''
    return list(set(l))

def main():
    l = input('Enter your list: ')
    a = [x for x in l.split()]
    choice = input("Enter '1' for set method and '2' for loop method: ")
    if choice == 1:
        set_way(l)
    else:
        duplicates(l)

if __name__ == '__main__':
    main()