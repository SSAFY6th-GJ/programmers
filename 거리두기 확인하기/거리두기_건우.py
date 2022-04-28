# di = [0, 0, -1, 1]
# dj = [1, -1, 0, 0]

# def dfs(x,y,dis):
# 	st = [(x,y)]
# 	while st:
# 		i, j, dis = st.pop()
# 		for d in range(4):
# 			new_i = i + di[d]
# 			new_j = j + dj[d]
# 			if 0 <= new_i < 5 and 0 <= new_j  <5 and place[new_i][new_j] != 'X':
# 				st.append((new_i,new_j))

# def solution(places):
# 	answer = []
# 	for place in places:
# 		player = []
# 		for i in range(5):
# 			for j in range(5):
# 				if place[i][j] == 'P':
# 					player.append((i,j))
# 		for pos in player:
# 			i, j = pos[0], pos[1]

# 	return answer


from collections import deque

di = [-1, 1, 0, 0]  
dj = [0, 0, -1, 1] 
def bfs(p):
    start = []
    
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])
    
    for s in start:
        que = deque([s]) 
        visited = [[0]*5 for i in range(5)]   
        distance = [[0]*5 for i in range(5)] 
        visited[s[0]][s[1]] = 1
        
        while que:
            i, j = que.popleft()
            for d in range(4):
                new_i = i + di[d]
                new_j = j + dj[d]

                if 0<=new_i<5 and 0<=new_j<5 and visited[new_i][new_j] == 0:
                    
                    if p[new_i][new_j] == 'O':
                        que.append([new_i, new_j])
                        visited[new_i][new_j] = 1
                        distance[new_i][new_i] = distance[i][j] + 1
                    
                    if p[new_i][new_j] == 'P' and distance[new_i][new_j] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    
    for place in places:
        answer.append(bfs(place))
    
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
				["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
				["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
				["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
				["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))