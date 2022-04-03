'''
문자열 p를 u, v로 분리하는 함수와 문자열 u가 올바른 괄호 문자열인지 확인하는 함수를 작성한 뒤
문제에 서술되어 있는 로직을 그대로 구현
'''

def divide(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i + 1], p[i + 1:]

def isCor(p):
    stack = []
    for c in p:
        if c == '(':
            stack.append(c)
        else:
            if not len(stack):
                return False
            stack.pop()
    return True

def solution(p):
    if len(p) == 0:
        return p
    u, v = divide(p)
    if isCor(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

    return answer

