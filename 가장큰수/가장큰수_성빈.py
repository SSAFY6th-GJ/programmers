def solution(numbers):
    numbers.sort()
    answer = ''
    result = []
    cnt = 0
    while cnt != len(numbers):
        cnt += 1
        maxv = '0'
        for i in range(len(numbers)):
            if str(numbers[i]) in result:
                continue
            if maxv < str(numbers[i]):
                if len(maxv) <= len(str(numbers[i])):
                    maxv = str(numbers[i])
        print(result)
        answer += maxv
        result.append(maxv)

    return answer