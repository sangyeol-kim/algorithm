# 단순탐색 (Simple Search)
# 앞에서부터 원하는게 나올 때 까지 하나하나 찾는다.

# 만들기 쉽고 정렬이 안되어 있어도 된다.

# 느림
# O(n)

# 대안은 이진탐색(Binary Search)

arr = [1, 2, 3, 5, 6, 8, 9, 10, 12]

def simpleSearch(list, target):
    for i in range(0, len(list)):
        if (list[i] == target):
            print(target, "는", i+1, "번째에 있습니다")


simpleSearch(arr, 8)
