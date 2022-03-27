# 정답아님

def solution(progresses, speeds):
    res = []
    check = 0
    while len(progresses) > 0:
        ans = 0

        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            check += 1
        else:
            if check > 0:
                res.append(check)
                check = 0

    res.append(check)
    return res