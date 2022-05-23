def solution(d, budget):
    d.sort()
    cnt = 0
    for x in range(len(d)):
        if budget >= d[x]:
            budget -= d[x]
            cnt += 1
        else:
            break
    return cnt