def solution(s):
    numbers = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
              'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'
              }
    tmp = ''
    ans = ''
    for x in range(len(s)):
        if s[x].isdigit() == False:
            tmp += s[x]
            for y in numbers.keys():
                if y == tmp:
                    ans += numbers[tmp]
                    tmp = ''
        elif s[x].isdigit() == True:
            ans += s[x]
    return int(ans)