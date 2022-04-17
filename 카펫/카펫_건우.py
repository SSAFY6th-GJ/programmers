brown = 24
yellow = 24
yellow_divide = []
res = []
for i in range(1,yellow+1):
  if yellow % i ==0:
    yellow_divide.append(i)
print(yellow_divide)
for j in range(len(yellow_divide)):
  garo = yellow_divide[len(yellow_divide) - j -1]
  sero = yellow_divide[j]
  if (garo + sero) * 2 + 4 == brown:
    res.append(garo+2)
    res.append(sero+2)
    break
print(res)