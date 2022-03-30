# 정답 아님
def solution(phone_book):
    for x in range(len(phone_book)):
        length_x = len(phone_book[x])

        for y in range(len(phone_book)):
            length_y = len(phone_book[y])

            if x != y:
                if phone_book[y][0:length_x] == phone_book[x]:
                    return False
    return True