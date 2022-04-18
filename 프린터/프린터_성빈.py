def solution(priorities, location):
    answer = 0
    # lst = []
    # num = [0]*(len(priorities))
    # cnt = 0
    while len(priorities) != 0:
        if location==0: # 출력해야할게 제일 앞에 있을 때
            if priorities[0] < max(priorities): # 더 중요한 문서가 있다면
                priorities.append(priorities.pop(0)) # 맨 뒤로 보냄
                location=len(priorities)-1 # location을 맨 끝으로 바꿈
            else: # 더 중요한 문서가 없다면 출력해야 함
                return answer+1
        else: # 출력해야할게 제일 앞이 아니면
            if priorities[0] < max(priorities): # 더 중요한 문서가 있다면
                priorities.append(priorities.pop(0)) # 맨 뒤로 보내고
                location -= 1 # 맨 앞에 있던게 맨 뒤로 갔으니까 location -1
            else:
                priorities.pop(0) # 맨 앞에 있는게 가장 중요한 문서니까 출력
                location -= 1 # 맨 앞에 있던게 출력되서 location -1
                answer += 1

    return answer