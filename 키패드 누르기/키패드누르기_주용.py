def solution(numbers, hand):
    result = ''
    place = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1],
             9:[2,2], '*':[3,0], 0: [3,1], '#':[3,2]}
    L = place['*']
    R = place['#']
    for x in numbers:
        if x == 1 or x == 4 or x == 7:
            result += 'L'
            L = place[x]
        elif x == 3 or x == 6 or x == 9:
            result += 'R'
            R = place[x]
        else:
            far_L = abs(place[x][0]-L[0]) + abs(place[x][1]-L[1])
            far_R = abs(place[x][0]-R[0]) + abs(place[x][1]-R[1])
            if far_L == far_R:
                if hand == 'left':
                    result += 'L'
                    L = place[x]
                elif hand == 'right':
                    result += 'R'
                    R = place[x]
            elif far_L > far_R:
                result += 'R'
                R = place[x]
            elif far_L < far_R:
                result += 'L'
                L = place[x]
    return result