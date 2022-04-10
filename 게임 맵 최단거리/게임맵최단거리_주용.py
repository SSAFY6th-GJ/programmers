# 왜 런타임에러 뜨지

from collections import deque


def solution(maps):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    row_num = len(maps)
    col_num = len(maps[0])
    arr = [[-1] * col_num for _ in range(row_num)]
    arr[0][0] = 1

    def bfs(c, r):
        queue = deque()
        queue.append((c, r))

        while queue:
            c, r = queue.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < row_num and 0 <= nc < col_num and maps[nc][nr] == 1:
                    if arr[nc][nr] == -1:
                        arr[nc][nr] = arr[c][r] + 1
                        queue.append((nc, nr))

    bfs(0, 0)
    answer = arr[col_num - 1][row_num - 1]
    return answer