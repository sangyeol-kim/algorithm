

def rec(list, accu):
    if (len(list) == 0):
        return accu
    else:
        last = list.pop()
        result = accu + last
        return rec(list, result)


numbers = input()
items = [int(num) for num in numbers.split()]

result = rec(items, 0)
print(result)
