# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

# 예제 입력 1 
# 4
# 1 3 5 7
# 예제 출력 1 
# 3


# 초안 코드
# Output은 잘 나오나 틀린 답이라고 나옴
# import sys

# s = sys.stdin.readline

# number = int(s())
# numbers = s()

# number_list = [int(num) for num in numbers.split()]

# def prime(number_list):
#   for i in number_list:
#     if i == 1:
#       number_list.remove(i)
#       break
#     elif i == 2:
#       break
#     temp = 2
#     while temp < i:
#       if i % temp == 0:
#         number_list.remove(i)
#         break
#       else:
#         temp += 1
#         break
#   return len(number_list)

# print(prime(number_list))


# 수정 코드
import sys

s = sys.stdin.readline

number = int(s())
numbers = s()

number_list = [int(num) for num in numbers.split()]

def prime(number_list):
  res = 0
  if len(number_list) == number:
    for i in number_list:
      count = 0
      for j in range(1, i+1):
        if i % j == 0:
          count += 1
      if count == 2:
        res += 1
    return res
  else:
    return -1

print(prime(number_list))