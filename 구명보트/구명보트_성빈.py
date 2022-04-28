def solution(people, limit):
    answer = 0
    people.sort()

    first = 0
    last = len(people) - 1

    while first <= last:
        answer += 1
        if people[first] + people[last] <= limit:
            first += 1
            last -= 1

    return answer


'''
구명보트는 작아서 한번에 최대 2명씩 만 가능
최대 + 최소 조합으로 보트에 태워봐야하니까
무게를 오름차순으로 정렬함
최대+최소로 태웠는데 무게 초과하면 혼자만 태운다

'''