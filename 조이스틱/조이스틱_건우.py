# di = [1, -1]
# name = "JEROEN"
# # print(ord('A'))
# # print(ord('Z'))
# cnt_list = []
# visited = []
# for i in name:
#   cnt = ord(i) - ord('A')
#   if cnt > 13:
#     cnt = 13- (cnt - 13)
#   cnt_list.append(cnt)
# for k in cnt_list:
#   if k == 0:
#     visited.append(True)
#   else:
#     visited.append(False)


# def dfs(now_pos, change_cnt):
#   global min_chage_cnt
#   if change_cnt >= min_chage_cnt:
#     return
#   visited[now_pos] = True
#   change_cnt += 1
#   if False in visited:
#     for d in range(2):
#       new_pos = now_pos + di[d]
#       if new_pos < 0:
#         new_pos = len(cnt_list) - 1
#       elif new_pos >= len(cnt_list):
#           new_pos = 0
      
#       if visited[new_pos] == False:
#         change_again = True
#       else:
#         change_again = False
#       dfs(new_pos,change_cnt)
#       if change_again:
#         visited[new_pos] = False
#   else:
#     min_chage_cnt = change_cnt

# min_chage_cnt = len(cnt_list)-1
# dfs(0, -1)
# print(min_chage_cnt)
# print(sum(cnt_list))



# def dfs():
#   st = []
#   st.append((0,0))
#   while st:
#     now_pos, change_cnt = st.pop()
#     visited[now_pos] = True
#     if False in visited:
#       for d in range(2):
#         new_pos = now_pos + di[d]
#         if new_pos < 0:
#           new_pos = len(cnt_list) - 1
#         elif new_pos >= len(cnt_list):
#           new_pos = 0
#         st.append((new_pos,change_cnt+1))
#     else:
#       cnt_list_2.append(change_cnt)
def solution(name):
    global min_change_cnt
    answer = 0

    di = [-1, 1]
    cnt_list = []
    visited = []
    for i in name:
      cnt = ord(i) - ord('A')
      if cnt > 13:
        cnt = 13- (cnt - 13)
      cnt_list.append(cnt)
    for k in cnt_list:
      if k == 0:
        visited.append(True)
      else:
        visited.append(False)

    min_change_cnt = len(cnt_list)
    def dfs(now_pos, change_cnt):
      global min_change_cnt
      if change_cnt >= min_change_cnt:
        return
      visited[now_pos] = True
      change_cnt += 1
      if False in visited:
        for d in range(2):
          new_pos = now_pos + di[d]
          if new_pos < 0:
            new_pos = len(cnt_list) - 1
          elif new_pos >= len(cnt_list):
            new_pos = 0
          
          if visited[new_pos] == False:
            change_again = True
          else:
            change_again = False
          dfs(new_pos,change_cnt)
        
          if change_again:
            visited[new_pos] = False
      else:
        min_change_cnt = change_cnt


    dfs(0, -1)
    answer = sum(cnt_list) + min_change_cnt
    return answer