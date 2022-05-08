def solution(N, stages):
	answer = []
	fail_rate = [0] * N
	for i in range(N):
		challengers = 0
		uncomplete = 0
		for stage in stages:
			if stage >= i+1:
				challengers += 1
				if stage == i+1:
					uncomplete += 1
		if challengers == 0:
			fail_rate[i] = 0
		else:
			fail_rate[i] = uncomplete / challengers
		print(uncomplete,challengers)
	print(fail_rate)
	return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
solution(N,stages)