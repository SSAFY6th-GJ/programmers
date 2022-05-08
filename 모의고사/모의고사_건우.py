def solution(answers):
	res = []
	res_1 = 0
	res_2 = 0
	res_3 = 0
	my_answer_1 = [1, 2, 3, 4, 5]
	my_answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
	my_answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
	for i in range(len(answers)):
		if answers[i] == my_answer_1[i%5]:
			res_1 += 1
		if answers[i] == my_answer_2[i%8]:
			res_2 += 1
		if answers[i] == my_answer_2[i%10]:
			res_3 += 1
	max_res = max(res_1, res_2, res_3)
	if res_1 == max_res:
		res.append(1)
	if res_2 == max_res:
		res.append(2)
	if res_3 == max_res:
		res.append(3)
	print(max_res)
	return res

answers = [1,3,2,4,2]
print(solution(answers))