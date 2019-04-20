arr = [1,2,3]

for i in range(0, len(arr)):
  if arr[i] == 2:
    print(i, "찾음")
    break
  elif arr[i] != 2:
    print(i, "아님")