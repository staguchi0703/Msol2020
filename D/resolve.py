def resolve():
    '''
    code here
    '''
    N = int(input())
    As = [int(item) for item in input().split()]

    deff_list = [0]
    for i in range(1,N):
        deff_list.append(As[i] - As[i-1])

    prev = 1000
    res = 1000
    for i in range(1, N):
        if deff_list[i] >= 0:
            res = (prev // As[i-1]) * As[i] + prev % As[i-1]
        
        prev = res
    
    print(res)



if __name__ == "__main__":
    resolve()
