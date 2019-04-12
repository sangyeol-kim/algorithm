# Dynamic Programming

# Memoization
# 결과값을 메모한다.
# 함수 호출은 비용이 크기 때문에 함수 호출을 적게 하는 방법
# 메모 해놓은 값을 넘겨서 이미 계산한 값을 다시 안하도록


def fib(n):
    if n <= 1:
        memo[n] = n

    if n not in memo:
        memo[n] = fib(n-2) + fib(n-1)

    return memo[n]


memo = {}
print(fib(6))
