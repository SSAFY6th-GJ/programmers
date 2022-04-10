def solution(numbers):
    # numbers.sort()
    # answer = ''
    # result = []
    # cnt = 0
    # while cnt != len(numbers):
    #     cnt += 1
    #     maxv = '0'
    #     for i in range(len(numbers)):
    #         if str(numbers[i]) in result:
    #             continue
    #         if maxv < str(numbers[i]):
    #             if len(maxv) <= len(str(numbers[i])):
    #                 maxv = str(numbers[i])
    #     print(result)
    #     answer += maxv
    #     result.append(maxv)
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    # numbers 인자 각각의 문자열을 3번 반복한다. numbres의 인수의 범위가 1000이하니까 3자리로 맞춘 뒤 비교
    # 101010, 666, 222 -> 666, 222, 101010
    # 문자열 비교는 아스키코드로 치환되어 정렬된다. reverse로 내림차순 정렬해준 뒤 join으로 합쳐준다
    answer = str(int(''.join(numbers)))
    # 모든 값이 0일때 int로 변환한 뒤 다시 str로 변환하여 처리해주기 위해

    return answer