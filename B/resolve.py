def resolve():
    '''
    code here
    '''
    A, B, C = [int(item) for item in input().split()]
    K = int(input())
    is_flag = False
    for i in range(K+1):
        for j in range(K+1):
            if i+j <= K:
                if A*2**i < B*2**j < C*2**(K-(i+j)):
                    is_flag = True
    
    print('Yes') if is_flag else print('No')


if __name__ == "__main__":
    resolve()
