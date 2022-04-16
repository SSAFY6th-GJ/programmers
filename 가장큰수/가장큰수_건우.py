# def solution(numbers):
#   answer = ''
#   numbers_str =[]
#   for i in numbers:
#       numbers_str.append(str(i))
#   print(numbers_str)
#   for num in numbers_str:
#     lst =[]
#     for j in range(9, 0, -1):
#         if num[0] == str(j):
#             lst.append(num)
#   print(lst)            
#   return answer

# solution([3, 30, 34, 5, 9])

a = sorted(['12', '95', '954', '997', '969', '9', '997'], reverse=True)
print(a)