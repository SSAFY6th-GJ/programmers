def solution(brown, yellow):
    answer = []
    x = 0
    y = 0
    res = set()
    res.add((yellow, 1))
    for i in range(1, yellow // 2):
        if yellow % i == 0:
            y = i
            x = yellow // i
            if x >= y:
                res.add((x, y))
    res = list(res)
    for i in range(len(res)):
        if brown == ((res[i][0] + 2) * 2 + res[i][1] * 2):
            answer.append(res[i][0] + 2)
            answer.append(res[i][1] + 2)

    return answer