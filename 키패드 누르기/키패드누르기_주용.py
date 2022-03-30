def solution(numbers, hand):
    result = ''
    place = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1],
             9:[2,2], '*':[3,0], 0: [3,1], '#':[3,2]}
    L = place['*']
    R = place['#']
    for x in numbers:
        if x == 1 or x == 4 or x == 7:
            result += 'L'
            L = place[x]        # 위치저장
        elif x == 3 or x == 6 or x == 9:
            result += 'R'
            R = place[x]        # 위치저장
        else:
            far_L = abs(place[x][0]-L[0]) + abs(place[x][1]-L[1])   # x좌표 y좌표 각각 차이의 절댓값
            far_R = abs(place[x][0]-R[0]) + abs(place[x][1]-R[1])   # x좌표 y좌표 각각 차이의 절댓값
            if far_L == far_R:      # 거리가 같으면
                if hand == 'left':  # 왼손잡이는
                    result += 'L'   # 왼손으로
                    L = place[x]    # 위치 저장
                elif hand == 'right':   # 오른손 잡이는
                    result += 'R'       # 오른손으로
                    R = place[x]    # 위치저장
            elif far_L > far_R:     # L이 거리가 더 멀다
                result += 'R'       # 오른손으로 누른다
                R = place[x]    # 위치저장
            elif far_L < far_R:     # R이 거리가 더 멀다
                result += 'L'       # 왼손으로 누른다
                L = place[x]    # 위치저장
    return result