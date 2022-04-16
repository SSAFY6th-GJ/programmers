from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    answer = 0

    
    def dfs(x,y):
        st =deque()
        st.append((x,y))
        while st:
            cur_i, cur_j = st.popleft()
            visited[cur_i][cur_j] = True
            if cur_i == n-1 and cur_j == m-1:
                return
            for d in range(4):
                new_i = cur_i + di[d]
                new_j = cur_j + dj[d]
                if 0 <= new_i < n and 0 <= new_j < m and maps[new_i][new_j] !=0 and not visited[new_i][new_j]:
                    st.append((new_i,new_j))
                    maps[new_i][new_j] = maps[cur_i][cur_j] + 1
    dfs(0,0)
    
    answer = maps[n-1][m-1]
    if answer == 1:
      answer = -1
    return answer