def solution(progresses, speeds):
    answer = []
    sumv = len(progresses)
    while sumv != sum(answer):
        cnt = 0
        while progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                cnt += 1
            elif progresses[i] < 100:
                break
        answer.append(cnt)
        for _ in range(cnt):
            progresses.pop(0)
            speeds.pop(0)
            if len(progresses) == 0:
                break
        if len(progresses) == 1:
            answer.append(1)

    return answer

'''
0번째 원소가 100 같거나 넘을때까지 speed를 더해준다
0번째가 넘었을때 배열을 전체 돌면서 100 넘은 원소 개수를 세준다
100 안넘은 원소가 나오면 거기서 반복문 break
세준 개수를 정답배열에 넣어준다.
세준 개수만큼 progresses 배열에서 원소를 pop 해줌
처음 progresses 배열의 개수와 정답 배열의 합이 같아질때까지 while문 돌려준다.
중간중간 print 찍어보고 예외처리 하느라 시간 개오래걸림
'''