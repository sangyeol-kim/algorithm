
def bubble(list):
    temp = 0
    for i in range(0, len(list)):  # 0~3
        for j in range(i+1, len(list)):  # i~3
            if (list[i] > list[j]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list


numbers = input()
items = [int(num) for num in numbers.split()]

print(bubble(items))
