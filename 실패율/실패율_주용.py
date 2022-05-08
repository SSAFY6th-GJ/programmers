def solution(N, stages):
    fail = {}
    user_cnt = len(stages)

    for i in range(1, N + 1):
        if user_cnt != 0:
            fail_user = stages.count(i)
            fail[i] = fail_user / user_cnt
            user_cnt -= fail_user
        else:
            fail[i] = 0
    return sorted(fail, reverse=True, key=lambda x: fail[x])