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


def solution(m, musicinfos):
    res = []
    list_m = []  
    for  k in m:                  #문자열로 들어와 있는 m을 리스트로 바꿔준다 이때 c # 이면 따로따로 따로 들어오므로 #은 별도 처리해준다
        if k == '#':
            list_m[-1] += k
        else:
            list_m.append(k)
    for info in musicinfos:
        time1, time2, subject, melody = info.split(',')        # 시간을 빼서 분으로 구해준다
        playtime = (int(time2[0:2]) - int(time1[0:2])) * 60 + int(time2[3:5])- int(time1[3:5])
        play_melody = []
        list_melody = []
        for m in melody:
            if m == '#':                     # 문자열로 들어온 것은 리스트로 바꿔준다 마찬가지로 # 은 별도 처리해준다
                list_melody[-1] += m
            else:
                list_melody.append(m)
        for i in range(playtime):              # 플레이 타임 동안 음악이 반복되므로 플레이 시간동안 어떤 멜로디가 나오는지 기록해준다.
            pos = i
            while pos >= len(list_melody):
                pos -= len(list_melody)
            play_melody.append(list_melody[pos])
        for j in range(len(play_melody)-len(list_m)+1):     #플레이 시간 동안 나온 멜로디 안에 음악이 있는지 확인해준다.
            if list_m == play_melody[j: j+len(list_m)]:
                if not res:
                    res.append((subject,playtime))
                else:
                    if res[0][1] < playtime:                 
                        res = [(subject, playtime)]
                     
    if not res:                                      # 맞는 음악이 없으면 none
        answer = '(None)'
    else:
        answer = res[0][0]
        
    return answer