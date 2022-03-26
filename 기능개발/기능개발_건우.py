def solution(progresses, speeds):
    answer = []
    finish = []
    for i in range(len(progresses)):
        finish_work = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] > 0:
            finish_work += 1
        finish.append(finish_work)
    finish.append(100)
    day = finish[0]
    pos = 0
    count = 0
    while pos < len(finish) - 1:
        while finish[pos] <= day:
            pos += 1
            count += 1
        answer.append(count)
        day = finish[pos]
        count = 0
    return answer

print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
