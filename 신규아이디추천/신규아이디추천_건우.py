def solution(new_id):
	answer_1 = ''
	#step 1
	for i in new_id:
		if 65 <= ord(i) <= 90:
			answer_1 += chr(ord(i)+32)
		else:
			answer_1 += i
	#step 2
	answer_2 = ''
	for i in answer_1:
		if i in['-', '_', '.'] or i.isalpha() or i.isdigit():
			answer_2 += i
	#step 3
	answer_3 = ''
	for i in range(len(answer_2)-1):
		if answer_2[i] == '.':
			if answer_2[i+1] == '.':
				pass
			else:
				answer_3 += '.'
		else:
			answer_3 += answer_2[i]
	answer_3 += answer_2[-1]
	#step 4
	answer_4 = ''
	if answer_3[0] == '.':
		answer_4 = answer_3[1:]
	else:
		answer_4 = answer_3
	if answer_4:
		if answer_4[-1] == '.':
			answer_4 = answer_4[:-1]
	# step5
	answer_5 = ''
	if not answer_4:
		answer_5 = 'a'
	else:
		answer_5 = answer_4
	
	#step6
	answer_6 = ''
	if len(answer_5) >= 16:
		answer_6 = answer_5[:15]
	else:
		answer_6 = answer_5
	if answer_6[-1] == '.':
		answer_6 = answer_6[:-1]
	#step 7
	answer_7 = ''
	answer_7 = answer_6
	if len(answer_6) <= 2:
		while len(answer_7) < 3:
			answer_7 += answer_6[-1]

		
	return answer_7

new_id = "=.="
print(solution(new_id))