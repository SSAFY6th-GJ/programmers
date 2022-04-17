def solution(brown, yellow):
    total = brown + yellow

    ans = []
    # 세로를 1부터 탐색(가로 >= 세로)
    for x in range(1, total + 1):  # x == 세로
        if total % x == 0:
            width = total // x  # width == 가로
            if width >= x:
                if (width - 2) * 2 + x * 2 == brown:
                    ans.append(width)
                    ans.append(x)
                    break

    return ans