def fib(n):
  for i in range(0, n+1):
    if i <= 1:
      list.append(i)
    else:
      list.append(list[i-2] + list[i-1])
  return list[-1]

n = int(input())

list = []

print(fib(n))