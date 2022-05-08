def solution(n, lost, reserve):
    answer = 0
    clothes = [0] + [1] * n
    for i in lost:
        clothes[i] = 0
    for j in reserve:
        clothes[j] += 1
    for k in range(1,len(clothes)-1):
        if clothes[k] == 0:
            if clothes[k-1] == 2:
                clothes[k-1] -= 1
                clothes[k] = 1
            elif clothes[k+1] == 2:
                clothes[k+1] -= 1
                clothes[k] = 1
    answer = clothes.count(1) + clothes.count(2)
    
    return answer


n = 5
lost = [2,4]
reserve = [1, 3, 5]

print(solution(n,lost,reserve))