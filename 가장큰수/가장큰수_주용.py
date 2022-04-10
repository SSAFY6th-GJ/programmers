def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
    # 333 303030 343434 555 999
    # 이거 말고 다른 방법 생각해봤는데 딱히 생각 안난다
    # numbers = list(map(str, numbers))
    # base = []
    # for x in range(len(numbers)):
    #     a = int(str(numbers[x] * 3)[:3])
    #     # 크기를 비교해서 그 번호의 인덱스로 순서 저장하고 ...하는 거보다
    #     # 그냥 lambda로 하는게 제일 깔끔한거 같다.
    #     base.append(a)
    # base.sort(reverse=True)
