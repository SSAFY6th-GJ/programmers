def solution(new_id):
    answer = ''

    # 1단계: 모두 소문자
    new_id = new_id.lower()

    # 2단계: 소문자, 숫자, -,_,. 빼고 다 삭제
    for i in new_id:
        if i.islower() or i.isdigit() or i in ["-", "_", "."]:
            answer += i

    # 3단계: 점 두번 연속 나오면 점 하나로 바꿈
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계: 처음이나 끝에 . 있으면 삭제
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]

    # 5단계: 빈 문자열이면 a 넣어줌
    if answer == '':
        answer = 'a'

    # 6단계: 16개 이상이면 처음부터 15개까지만 남긴다. 제일 끝자리에 . 있으면 그것도 없앤다
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계: 2글자 이하이면 제일 마지막 문자를 길이가 3 될때까지 붙여준다
    if len(answer) < 3:
        answer = answer + answer[-1] * (3 - len(answer))
    return answer