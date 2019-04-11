# 이진탐색 (Binary Search)
# 탐색 범위를 절반씩 줄여나가면서 찾는다

# 빠르다

# 단점은 정렬이 되어 있어야 한다

# O(log n)

arr = [1, 2, 3, 4, 6, 8, 9, 10, 11, 12]


def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


print(binarySearch(arr, 15))