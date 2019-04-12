arr = [1, 2, 3, 4, 5, 6, 7]


def pick(arr):
    list = []
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            list.append((arr[i], arr[j]))
    return list


print(pick(arr))
