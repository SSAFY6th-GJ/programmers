from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(place, y, x):
    visited = [[False] * 5 for _ in range(5)]
    q = deque()
    q.append((y, x, 0))
    visited[y][x] = 1

    while q:


def check(p):
    for y in range(5):
        for x in range(5):
            if p[y][x] == 'P':
                if bfs(p, y, x) == False:
                    return False
    return True


def solution(places):
    answer = []

    for p in places:
        if check(p):
            answer.append(1)
        else:
            answer.append(0)

    return answer


'''
교실을 돌면서 P이면 bfs로 1칸, 2칸 탐색함
1,2칸 안에 다른 P가 있으면 거기서 탐색 멈추고 False반환

'''