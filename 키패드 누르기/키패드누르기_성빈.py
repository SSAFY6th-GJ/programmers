def solution(numbers, hand):
    answer = ''
    key=[[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    idx = []
    left = [3,0]
    right = [3,2]
    for i in range(len(numbers)):
        for a in range(4):
            for b in range(3):
                if numbers[i] == key[a][b]:
                    idx.append([a,b])
    print(idx)
    for i in range(len(idx)): # 0 1 2 3 4 ... 11
        if idx[i][1] == 0:
            answer += 'L'
            left = idx[i]
        elif idx[i][1] == 2:
            answer += 'R'
            right = idx[i]
        else:
            dis_l = abs(left[0]-idx[i][0]) + abs(left[1]-idx[i][1])
            dis_r = abs(right[0]-idx[i][0]) + abs(right[1]-idx[i][1])
            if dis_l > dis_r:
                answer += 'R'
                right = idx[i]
            elif dis_l < dis_r:
                answer += 'L'
                left = idx[i]
            else:
                if hand == "right":
                    answer += 'R'
                    right = idx[i]
                else:
                    answer += 'L'
                    left = idx[i]
    print(answer)
    return answer

# solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left")

'''
numbers 들을 모두 키패드 위치 배열로 받아서 
번호를 찍을 때마다 왼손, 오른손의 위치를 업데이트 시켜줬다.
눌러야 할 번호가 왼쪽 가운데 오른쪽에 있을때를 조건문 처리 해서
왼쪽에 있을때는 왼손, 오른쪽에 있을때는 오른손
가운데에 있을때는 왼손의 위치와 오른손의 위치의 거리를 따져서
더 가까운 손이 누르게 함
'''