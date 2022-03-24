def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if str(signs[i]) == 'True':
            answer += absolutes[i]
        elif str(signs[i]) == 'False':
            answer -= absolutes[i]
    return answer

'''
주어진 signs는 [true, false] 인데
왜 True False 로 조건문을 걸어야 통과인지 ..?
'''