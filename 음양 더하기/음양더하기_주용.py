def solution(absolutes, signs):
    ans = 0
    for x in range(len(absolutes)):
        if signs[x] == True:
            ans += absolutes[x]
        else:
            ans -= absolutes[x]
    return ans