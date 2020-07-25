def resolve():
    '''
    code here
    '''
    X = int(input())
    
    X = X//100

    if X < 6:
        res = 8
    elif X < 8:
        res = 7
    elif X < 10:
        res = 6
    elif X < 12:
        res = 5
    elif X < 14:
        res = 4
    elif X < 16:
        res = 3
    elif X < 18:
        res = 2
    else:
        res = 1
    print(res)

if __name__ == "__main__":
    resolve()
