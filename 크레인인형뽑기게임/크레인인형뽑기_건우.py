def solution(board, moves):
	answer = 0
	st = []
	for move in moves:
		move -= 1
		for i in range(len(board)):
			if board[i][move] != 0:
				st.append(board[i][move])
				board[i][move] = 0
				break
		if len(st) >= 2:
			if st[-1] == st[-2]:
				st.pop()
				st.pop()
				answer += 2
	return answer