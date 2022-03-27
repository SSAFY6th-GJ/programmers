def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4:3, 3: 4, 2:5, 1:6, 0:6}
    max_cnt = 0
    min_cnt = 0
    lottos.sort()
    win_nums.sort()
    res = []
    for x in range(6):
        if lottos[x] in win_nums:
            max_cnt += 1
            min_cnt += 1
        elif lottos[x] == 0:
            max_cnt += 1
    res.append(rank[max_cnt])
    res.append(rank[min_cnt])
    return res