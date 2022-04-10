from collections import deque


def solution(maps):
    N = len(maps)                           # 설명에서 1 <= N, M <= 100이고 N,M이 동시에 1인 경우는 없다고 했으므로
    M = len(maps[0])                        # 리스트의 길이, 리스트 내부 요소의 길이를 통해 N, M값을 얻는다.

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    Q = deque()
    Q.append((0, 0))

    while Q:                                # BFS 함수
        y, x = Q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                Q.append((ny, nx))

    if maps[N - 1][M - 1] == 1:             # 목표지점이 1인 경우 -1을 출력한다.
        answer = -1
    else:
        answer = maps[N - 1][M - 1]

    return answer