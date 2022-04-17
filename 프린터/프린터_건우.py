from collections import deque
def solution(priorities, location):
    check = [0] * len(priorities)
    check[location] = 1
    que = deque(priorities)
    check_que = deque(check)
    res = []
    check_res = []

    while que:
      a = que.popleft()
      b = check_que.popleft()
      if que:
        if a >= max(que):
          res.append(a)
          check_res.append(b)
        else:
          que.append(a)
          check_que.append(b)
      else:
        res.append(a)
        check_res.append(b)
    answer = check_res.index(1) + 1
    return answer