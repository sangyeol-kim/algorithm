def fib(n):
    result = []

    if (n <= 1):
        return n

    first = 1
    second = 1
    result.append(first)
    result.append(second)

    for i in range(2, n):
        third = first + second
        result.append(third)
        first = second
        second = third
    return result.pop()


print(fib(3))
