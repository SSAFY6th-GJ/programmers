def solution(numbers):
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in range(len(numbers)):
        if numbers[x] in num:
            num.remove(numbers[x])
    return sum(num)