def resolve():
    '''
    code here
    '''
    N = int(input())
    As = [int(item) for item in input().split()]

    deff_list = [0]
    for i in range(1,N):
        deff_list.append(As[i] - As[i-1])

    res_list = []
    is_first = True
    any_plus = False
    for i in range(1,N):
        if deff_list[i] > 0:
            any_plus = True
        
        if is_first and any_plus and deff_list[i] < 0 :
            res_list.append([i-1, As[i-1]])
            is_first = False

        if deff_list[i-1] > 0 and deff_list[i] < 0:
            res_list.append([i-1, As[i-1]])
        


    else:
        if deff_list[N-1] >= 0 and any_plus:
            res_list.append([N-1, As[N-1]])

    prev = 0
    res = 1000
    for i, val in res_list:
        if prev < i:
            temp_min = min(As[prev:i])
            temp_num = res //  temp_min
            res = temp_num * val + res % temp_min

        prev = i

    print(res)



if __name__ == "__main__":
    resolve()
