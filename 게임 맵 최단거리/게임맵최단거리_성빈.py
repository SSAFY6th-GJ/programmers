from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    visited = [[0] * (col) for _ in range(row)]
    visited[0][0] = 1

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    queue = deque()
    queue.append([0, 0])

    while queue:
        r, c = queue.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < row and 0 <= nc < col and maps[nr][nc] == 1:
                if visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append([nr, nc])

    answer = visited[-1][-1]
    if answer == 0:
        answer = -1
    return answer

# 전형적인 bfs 문제