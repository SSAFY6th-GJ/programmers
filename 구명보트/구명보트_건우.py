from collections import deque
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    people = deque(people)

    while people:
        is_limit = 0
        on_boat = []
        for person in people:
            if is_limit + person <= limit:
                is_limit += person
                on_boat.append(person)
        for i in on_boat:
          people.remove(i)
        answer += 1
            
        
    return answer

# def solution(people, limit):
#     answer = 0
#     people.sort(reverse=True)
#     people = deque(people)
#     lst = []
#     if len(people) % 2 == 1:
#       half = len(people) // 2 + 1
#     else:
#       half = len(people) // 2
#     for i in range(half):
#       lst.append(people.popleft())
#     while people:
#       person = people.popleft()
#       is_plus = False
#       for j in range(len(lst)):
#         if lst[j] + person <= limit:
#           lst[j] += person
#           is_plus = True
#           break
#       if not is_plus:
#         lst.append(person)
#     answer = len(lst)
#     return answer

people = [20, 30, 30, 50, 60, 70, 80, 90 ,100]
limit = 100
print(solution(people, limit))