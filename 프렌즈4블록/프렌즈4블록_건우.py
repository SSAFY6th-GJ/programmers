# def solution(m, n, board):
#     boards = []
#     for sen in board:
#         a = []
#         for alphabet in sen:
#             a.append(alphabet)
#         boards.append(a)
#     answer = 0
#     res = []
#     for i in range(m-1):
#         for j in range(n-1):
#             if  boards[i][j] == boards[i+1][j] == boards[i][j+1] == boards[i+1][j+1]:
#                 res.append((i,j))
#     for k in res:
#         x, y = k[0], k[1]
#         boards[x][y] =0
#         boards[x+1][y] = 0
#         boards[x][y+1] = 0
#         boards[x+1][y+1] = 0  
#     # return boards
#     boards_rotate=[]
#     for j in range(n-1,-1, -1):
#         b =[]
#         for i in range(m):
#             b.append(boards[i][j])
#         boards_rotate.append(b)
#     # return boards_rotate
    
#     for i in range(n):
#         cnt_0 = 0
#         for j in range(m):
#             if boards_rotate[i][j] == 0:
#                 cnt_0 += 1
#         for _ in range(cnt_0): 
#             boards_rotate[i].remove(0)
#         add_0 = [0] * cnt_0
#         boards_rotate[i] = add_0 + boards_rotate[i]
#     # return boards_rotate
#     boards = []
#     for j in range(m-1,-1,-1):
#         c =[]
#         for i in range(n):
#             c.append(boards_rotate[i][j])
#         boards.append(c)
#     return boards
# m, n = 6, 6
# board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
# print(solution(m,n,board))

from pprint import pprint 

def solution(m, n, board):
    boards = []
    for sen in board:
        a = []
        for alphabet in sen:
            a.append(alphabet)
        boards.append(a)
    answer = 0
    boards_rotate=[]
    # 회전하기
    for j in range(n-1,-1, -1):
        b =[]
        for i in range(m):
            b.append(boards[i][j])
        boards_rotate.append(b)
    pprint(boards)
    pprint(boards_rotate)
    removing = True
    while removing:
        res = []
        for i in range(n-1):
            for j in range(m-1):
                if boards_rotate[i][j] !=0 and boards_rotate[i][j] == boards_rotate[i+1][j] == boards_rotate[i][j+1] == boards_rotate[i+1][j+1]:
                    res.append((i,j))
        if not res:
            break
        for k in res:
            x, y = k[0], k[1]
            boards_rotate[x][y] =0
            boards_rotate[x+1][y] = 0
            boards_rotate[x][y+1] = 0
            boards_rotate[x+1][y+1] = 0  
        pprint(boards_rotate)
        for i in range(n):
            cnt_0 = 0
            for j in range(m):
                if boards_rotate[i][j] == 0:
                    cnt_0 += 1
            for _ in range(cnt_0): 
                boards_rotate[i].remove(0)
            add_0 = [0] * cnt_0
            boards_rotate[i] = add_0 + boards_rotate[i]
    answer = 0
    for lst in boards_rotate:
        answer += lst.count(0)
    print(answer)

m, n = 4, 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m,n,board))