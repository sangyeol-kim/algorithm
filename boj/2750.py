
# strList = []
# while True:
#     try:
#         strList.append(int(input('Enter the number > ')))
#     except ValueError:
#         print('Invalid number. Please try again!')
#         continue
# print(strList)


# def range(list):
#     print(list)
#     range_list = []
#     for num in range(0, len(list)):
#         if not range_list:
#             range_list.append(num)
#         elif num not in range_list:
#             range_list.append(num)
#         else:
#             break
#     return range_list


# print(range(strList))

number = int(input("몇개?"))
arr = []

for num in range(0, number):
    num = int(input(">"))
    arr.append(num)
    arr.sort()

for num in range(0, len(arr)):
    print(arr[num])
