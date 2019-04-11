word = "test"


def letterCount(word):
    map = {}
    for alphabet in word:
        if map.get(alphabet) == None:
            map[alphabet] = 1
        else:
            map[alphabet] += 1
        print(map)
    max = -1
    for key in map:
        print("key=>", key, "value=>", map[key])
        if (map[key] > max):
            max = map[key]
    return max


print(letterCount(word))
