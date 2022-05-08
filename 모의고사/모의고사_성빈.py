def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == one[i % 5]:
            result[0] += 1
        if answers[i] == two[i % 8]:
            result[1] += 1
        if answers[i] == three[i % 10]:
            result[2] += 1
    max_result = max(result)
    for i in range(3):
        if max_result == result[i]:
            answer.append(i + 1)
    return answer

