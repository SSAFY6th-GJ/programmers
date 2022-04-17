# 답 아님

def solution(name):
    # Z 90 A 65
    start = 'A' * len(name)
    cnt = 0

    for i in range(len(name)):
        if name[i] != start[i]:
            cnt += min((ord(name[i]) - ord(start[i])), ord('Z') - ord(name[i]) + 1)
            cnt += 1
    return cnt