str = input().upper()
dic = {}
max_list = []

for i in str:
  if i not in dic.keys():
    dic[i] = 1
  else:
    dic[i] += 1

max = max(dic.values())

for key, val in dic.items():
  if val >= max:
    max = val
    max_list.append(key)

if len(max_list) == 1:
  print(max_list[0])
else:
  print("?")

