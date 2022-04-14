# 왜 런타임에러 뜨지
from collections import deque
def solution(maps):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    row_num = len(maps)
    col_num = len(maps[0])
    arr = [[-1] * col_num for _ in range(row_num)] # -1로 한 이유는 갈 방법이 없을때 그냥 -1 출력해주려고
    arr[0][0] = 1
    def bfs(r, c):
        queue = deque()
        queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < row_num and 0 <= nc < col_num and maps[nr][nc] == 1:
                    if arr[nr][nc] == -1:
                        arr[nr][nc] = arr[r][c] + 1
                        queue.append((nr, nc))
    bfs(0, 0)
    answer = arr[row_num - 1][col_num - 1]
    return answer