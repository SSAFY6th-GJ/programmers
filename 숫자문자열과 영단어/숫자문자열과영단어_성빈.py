number_dic = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def solution(s):
    answer = ''
    string = ''
    for i in s:
        if i.isdigit():
            answer += i
        else:
            string += i
            if string in number_dic:
                answer += number_dic[string]
                string = ''

    return int(answer)

'''
숫자면 바로 answer에 붙이고
문자면 하나씩 string에 붙이다가
ex)
t
tw
two
딕셔너리에 있으면 해당 숫자를 answer에 붙인 다음
string을 '' 로 초기화
'''