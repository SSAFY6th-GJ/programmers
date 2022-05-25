def solution(num):
    answer = 0
    while num != 1:
        answer += 1
        if num%2==0:
            num //= 2
        elif num%2!=0:
            num = (num * 3) + 1
    if answer >= 500:
        answer = -1
    return answer

'''
1이 아닐때 while문 계속 돌림
짝수면 2로 나누고
홀수면 3을 곱하고 1 더해주기
'''