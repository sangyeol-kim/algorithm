# 문제
# 버블 정렬이란, 두 인접한 원소를 검사하여 자리를 바꾸는 방식으로 길이가 N인 수열을 정렬하는 알고리즘이다. 버블 정렬은 아래와 같은 단계를 총 N번 진행하면 된다.
# 1. 첫 번째 값과 두 번째 값을 비교하여 첫 번째 값이 더 크면 자리를 바꾼다.
# 2. 두 번째 값과 세 번째 값을 비교하여 두 번째 값이 더 크면 자리를 바꾼다.
# …
# N. N - 1번째 값과 N번째 값을 비교하여 N - 1번째 값이 더 크면 자리를 바꾼다.
# 세찬이는 버블 정렬의 결과는 당연히 알기에 버블 정렬의 중간 과정을 알아보려고 한다. 하지만 N이 매우 크므로 위와 같은 단계를 K번 하면 시간이 오래 걸린다. 세찬이를 도와 버블 정렬의 중간 과정을 구하는 프로그램을 작성하여라.

# 입력
# 첫 번째 줄에는 N과 K가 주어진다.
# 두 번째 줄에는 처음 수열의 상태가 주어진다. 즉, 처음 수열을 이루는 N개의 정수가 공백을 사이로 두고 차례대로 주어진다.
# 1 ≤ N ≤ 100, 000
# 1 ≤ K ≤ N
# 수열의 각 항은 1 이상 1, 000, 000, 000 이하의 정수이다.

# 출력
# 위 단계를 K번 한 후 수열의 상태를 출력한다.

# 예제 입력 1
# 4 1
# 62 23 32 15
# 예제 출력 1
# 23 32 15 62

n_k = input()  # 4 1
n_k_s = [int(num) for num in n_k.split()]

progression = input()  # 62 23 32 15 => 23 32 15 62
progressions = [int(num) for num in progression.split()]


def bubble(n_k_s, progressions):
    for i in range(0, n_k_s[1]):
        for j in range(i, n_k_s[0]-1):
            if (progressions[j] > progressions[j+1]):
                temp = progressions[j]
                progressions[j] = progressions[j+1]
                progressions[j+1] = temp
    for k in progressions:
        print(k, end=" ")


bubble(n_k_s, progressions)
