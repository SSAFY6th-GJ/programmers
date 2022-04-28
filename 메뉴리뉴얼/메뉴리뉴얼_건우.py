def solution(orders, course):
	answer = []

	# orders.sort(key=lambda x:len(x))
	# print(orders)
	def combi(menu,l,s):
		if len(menu) == r:
			if menu in res:
				res[menu] += 1
			else:
				res[menu] = 1
			return
		for i in range(s, len(order)):
			menu += order[i]
			combi(menu,l+1, i+1)
			# menu = menu[0:-1]

	for r in course:
		res = {}
		for order in orders:
			order=sorted(order)
			combi('',0, 0)
		sorted_res = sorted(res.items(), key= lambda x:x[1], reverse= True)
		# print(sorted_res)
		if sorted_res and sorted_res[0][1] >= 2:
			cnt = sorted_res[0][1]
		else:
			cnt = 2
		for key, value in sorted_res:
			if value < cnt:
				break
			else:
				answer.append(key)
	answer.sort()	
	return answer





orders = ["XYZ", "XWY", "WXA"]                
course = [2,3,4]
print(solution(orders, course))



