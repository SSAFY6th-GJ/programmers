def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero = lottos.count(0)
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    for i in range(6):
        if lottos[i] in win_nums:
            win_nums.remove(lottos[i])
            cnt += 1
    last = rank[cnt]
    zero += cnt
    first = rank[zero]
    answer.append(first)
    answer.append(last)
    return answer

'''
랭킹 순위를 딕셔너리로 정의
일단 0 인게 다 틀렸을때가 최하위 순위이고,
0인게 전부 다 맞췄을때가 최상위 순위이다.
0으로 냅둔 처음 배열에서 정답 번호랑 맞는거 개수를 센게 최하위 순위이고,
0의 개수만큼 다 정답이라고 가정했을때가 최상위 순위로 넣어줌
'''