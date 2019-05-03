# 자연수 과 정수 가 주어졌을 때 이항 계수 를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 과 가 주어진다. (1 ≤  ≤ 10, 0 ≤  ≤ )

# 출력
#  를 출력한다.

# 예제 입력 1 
# 5 2
# 예제 출력 1 
# 10

numbers = input()
number_list = [int(n) for n in numbers.split()]

n = number_list[0]
k = number_list[1]

def fac(number):
  if number == 0:
    return 0
  if number == 1:
    return 1
  return number * fac(number-1)

def ehang(n, k):
  if k == 0 or n-k == 0:
    return 1
  bunja = fac(n)
  bunmo1 = fac(k)
  bunmo2 = fac(n-k)

  return bunja // (bunmo1*bunmo2)

print(ehang(n,k))

