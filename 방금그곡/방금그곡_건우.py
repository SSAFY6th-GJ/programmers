m ="CC#BCC#BCC#BCC#B"
musicinfos =["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
res = []
for info in musicinfos:
	list_m = []
	for  k in m:
		if k == '#':
			list_m[-1] += k
		else:
			list_m.append(k)

	time1, time2, subject, melody = info.split(',')
	playtime = (int(time2[0:2]) - int(time1[0:2])) * 60 + int(time2[3:5])- int(time1[3:5])
	list_melody = []
	for m in melody:
		if m == '#':
			list_melody[-1] += m
		else:
			list_melody.append(m)
	play_melody = []
	print(list_melody)
	# play_melody = ''
	for i in range(playtime):
		pos = i
		while pos >= len(list_melody):
			pos -= len(list_melody)
		# play_melody.append(melody[pos])
		play_melody.append(list_melody[pos])
	print(play_melody)
	for j in range(len(play_melody)-len(list_m)+1):
		if list_m == play_melody[j: j+len(list_m)]:
			if not res:
				res.append((subject,playtime))
			else:
				if res[0][1] < playtime:
					res = [(subject, playtime)]
# print(res)

# print(list_m)
print (res[0][0])
# print(sorted(res, key=lambda x : -x[1])[0][0])

# def solution(m, musicinfos):
#     answer = ''
#     res = []
#     for info in musicinfos:
#         time1, time2, subject, melody = info.split(',')
#         playtime = (int(time2[0:2]) - int(time1[0:2])) * 60 + int(time2[3:5])- int(time1[3:5])
#         play_melody = ''
#         for i in range(playtime):
#             pos = i
#             while pos >= len(melody):
#                 pos -= len(melody)
#             play_melody += melody[pos]

#         if m in play_melody:
#             res.append((subject, playtime))
#     if not res:
#         answer = '(None)'
#     else:
#     	answer = sorted(res, key=lambda x : x[1])[0][0]
#     return answer

# def solution(m, musicinfos):
#     answer = ''
#     res = []
#     m = list(m)
#     for info in musicinfos:
#         time1, time2, subject, melody = info.split(',')
#         playtime = (int(time2[0:2]) - int(time1[0:2])) * 60 + int(time2[3:5])- int(time1[3:5])
#         play_melody = []
#         for i in range(playtime):
#             pos = i
#             while pos >= len(melody):
#                 pos -= len(melody)
#             if melody[pos] == '#':
#                 play_melody[-1] += melody[pos]
#             else:
#                 play_melody.append(melody[pos])
# 			for j in range(len(play_melody)-len(m)):
# 			if m == play_melody[j: j+len(m)]:
# 				res.append((subject,playtime))        
#     if not res:
#         answer = '(None)'
#     else:
#         answer = sorted(res, key=lambda x : -x[1])[0][0]
#     return answer