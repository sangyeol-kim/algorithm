import collections


def solution(cryptogram):
    result = ''
    answer = collections.Counter(map(lambda x: x[0], cryptogram))
    for key, value in answer.items():
        if value == 1:
            result += key
        elif value % 2 != 0:
            result += key
    print(result)


solution("browoanoommnaon")
