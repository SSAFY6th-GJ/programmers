def solution(nums):
    pick_num = len(nums) // 2   # 집어야하는 총 폰켓몬 수
    ans = 0
    set_nums = set(nums)        # 폰켓몬 종류의 수
    if pick_num < len(set_nums):    # 집어야하는 수보다 종류가 많으면 다양하게 집을 수 있음
        ans = pick_num
    else:
        ans = len(set_nums)         # 종류의 수가 더 적으면 어쩔수 없이 종류의 수 만큼 뽑을 수 있음
    return ans