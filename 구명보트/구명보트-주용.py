def solution(people, limit):
    people.sort()
    ans = 0
    i = 0
    j = len(people) - 1
    # 이진탐색?
    while i <= j:
        ans += 1
        if people[i] + people[j] <= limit:  # 20 40 40 70 80 80 limit 보다 크면 큰값만 받는다
            i += 1
        j -= 1
    return ans

# 처음에는 앞에서부터 구명보트에 태우면 된다고 생각
# def solution(people, limit):
#     people.sort()
#     ans = 0
#     tmp_sum = 0
#     for x in range(len(people)):
#         if tmp_sum+people[x] < limit:
#             tmp_sum += people[x]
#         elif tmp_sum+people[x] == limit:
#             ans += 1
#             tmp_sum = 0
#         elif tmp_sum+people[x] > limit:
#             ans += 1
#             tmp_sum = 0
#             tmp_sum += people[x]
#     if tmp_sum > 0:
#         ans += 1
#
#     return ans
