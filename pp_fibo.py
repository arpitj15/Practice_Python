#Practice Python Excercise 13

def fibo(n):
    '''Returns the fibonacci sequence to the given number of digits'''
    ans = [1,1]
    if n<3:
        return ans[:n]
    else:
        for i in range(2, n):
            ans.append(ans[i-1] + ans[i-2])
        return ans

def main():
    num = int(input('How many fibos do you want?: '))
    print(fibo(num))

if __name__ == '__main__':
    main()