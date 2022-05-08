def solution(board, moves):
    stack = []
    cnt = 0
    for x in moves:
        place = x - 1
        for y in range(len(board)):
            if board[y][place] != 0:
                pick = board[y][place]
                stack.append(pick)
                board[y][place]  = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop(-1)
                        stack.pop(-1)
                        cnt += 2
                break
    return cnt