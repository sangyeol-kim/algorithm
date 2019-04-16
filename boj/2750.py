number = int(input())
arr = []

for num in range(0, number):
    num = int(input())
    arr.append(num)
    arr.sort()

for num in range(0, len(arr)):
    print(arr[num])
