def solution(lottos, win_nums):
    answer = []
    score = 0
    for my in lottos:
        if my in win_nums:
            score += 1
    worst = score
    best = score + lottos.count(0)
    result = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    answer.append(result[best])
    answer.append(result[worst])
    return answer