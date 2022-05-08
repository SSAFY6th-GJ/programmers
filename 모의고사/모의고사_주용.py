def solution(answers):
    one = [1, 2, 3, 4, 5] * (10000 // 5)
    two = [2, 1, 2, 3, 2, 4, 2, 5] * (10000 // 8)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (10000 // 10)
    res = []
    s1 = 0
    s2 = 0
    s3 = 0
    for x in range(len(answers)):
        if answers[x] == one[x]:
            s1 += 1
        if answers[x] == two[x]:
            s2 += 1
        if answers[x] == three[x]:
            s3 += 1
    if max(s1, s2, s3) == s1:
        res.append(1)
    if max(s1, s2, s3) == s2:
        res.append(2)
    if max(s1, s2, s3) == s3:
        res.append(3)
    return res