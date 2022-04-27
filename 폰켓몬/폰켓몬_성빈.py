def solution(nums):
    answer = 0
    num = len(nums)//2
    mon = list(set(nums))
    print(mon)
    if len(mon) > num:
        answer = num
    else:
        answer = len(mon)
    return answer
'''
set으로 중복되는 번호 정리
중복되지 않은 포켓몬 수 구해서
N/2 마리가 중복되지않은 포켓몬의 수보다 많으면 중복되지않은 포켓몬 종류의 수 출력
N/2 마리가 중복되지 않은 포켓몬의 수보다 적으면 N/2 출력
'''