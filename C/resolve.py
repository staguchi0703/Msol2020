def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]
    As = [int(item) for item in input().split()]

    for i in range(K,N):
        if 1 < As[i] / As[i - K]:
            print('Yes')
        else:
            print('No')
        

if __name__ == "__main__":
    resolve()
