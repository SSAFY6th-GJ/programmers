def solution(numbers, hand):
    answer = ''
    distance_num ={2: {1 : 1, 2 : 0, 3 : 1, 4:2, 5:1, 6:2, 7:3, 8:2, 9:3, '*':4, 0 : 3, '#': 4},
                 5: {1 : 2, 2 : 1, 3 : 2, 4:1, 5:0, 6:1, 7:2, 8:1, 9:2, '*':3, 0 : 2, '#': 3},
                 8: {1 : 3, 2 : 2, 3 : 3, 4:2, 5:1, 6:2, 7:1, 8:0, 9:1, '*':2, 0 : 1, '#': 2}, 
                 0: {1 : 4, 2 : 3, 3 : 4, 4:3, 5:2, 6:3, 7:2, 8:1, 9:2, '*':1, 0 : 0, '#': 1}}
    pos_left = '*'
    pos_right = '#'
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            pos_left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            pos_right = num
        else:
            distance_left = distance_num[num][pos_left]
            distance_right = distance_num[num][pos_right]
            if distance_left < distance_right:
                answer += 'L'
                pos_left = num
            elif distance_left == distance_right:
                if hand == 'right':
                    answer += 'R'
                    pos_right = num
                else:
                    answer += 'L'
                    pos_left = num
            else:
                answer += 'R'
                pos_right = num
        
    return answer