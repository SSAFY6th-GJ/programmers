def solution(new_id):
    ans = ''
    # 1단계
    new_id = new_id.lower()
    # isalnum() 영어 or 한글 or 숫자  / isalpha() 영어 or 한글 / isdigit() 숫자
    # 2단계
    for x in range(len(new_id)):
        if new_id[x].isalnum() or new_id[x] in ['-', '_', '.']:
            ans += new_id[x]
    # 3단계
    while '..' in ans:
        ans = ans.replace('..', '.')
    # 4단계
    if ans[0] == '.':
        # 3번 예시에서 ans 에 '.' 만 들어오는데 len(ans) >= 2 조건 안주면 인덱스 에러난다
        if len(ans) >= 2:
            ans = ans[1:]
    if ans[-1] == '.':
        ans = ans[:-1]
    # 5단계
    if ans == '':
        ans = 'a'
    # 6단계
    if len(ans) >= 16:
        ans = ans[:15]
        if ans[-1] == '.':
            ans = ans[:-1]
    # 7단계
    if len(ans) <= 3:
        ans += ans[-1] * (3 - len(ans))

    return ans