def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        if budget < 0:
            break
        answer += 1
    return answer

'''
예산이 가장 적게 드는 부서부터 지원해주기.
오름차순으로 정렬하고 예산이 끝날때까지 돌려준다.
'''