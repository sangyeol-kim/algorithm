# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 예제 입력 1 
# 3 16
# 예제 출력 1 
# 3
# 5
# 7
# 11
# 13

import math

def prime(num):
  if num == 1:
    return False
  for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0:
      return False
  return True

m,n = map(int, input().split())
for j in range(m, n+1):
  if prime(j) == True:
    print(j)

# import math
 
# def isPrime(num):
#     if num == 1: return False
 
#     n = int(math.sqrt(num))
#     for k in range(2, n+1):
#         if num % k == 0: return False
#     return True
 
# # main
# m, n = map(int, input().split())
# for k in range(m, n+1):
#     if isPrime(k) : print(k)


