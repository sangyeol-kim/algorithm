# # n = input('A N: ')
# # n = int(n)
# # A = []
# # for i in range(n):
# #     pip = input('dice pips ' + str(i) + ':')
# #     pip = int(pip)

# #     # check pips input
# #     if pip < 1 or pip > 6:
# #         raise Exception('dice pips only 1 to 6!')

# #     A.append(pip)


def solution(A):
    def get_rotation(cur, target):
        if cur == 1:
            return 2 if target == 6 else 1
        elif cur == 2:
            return 2 if target == 5 else 1
        elif cur == 3:
            return 2 if target == 4 else 1
        elif cur == 4:
            return 2 if target == 3 else 1
        elif cur == 5:
            return 2 if target == 2 else 1
        elif cur == 6:
            return 2 if target == 1 else 1
        else:
            return 0  # error

    opt = 0
    for i, target in enumerate(A):
        rotation = 0
        for j, cur in enumerate(A):
            if i == j:
                continue

            if target == cur:
                continue

            rotation += get_rotation(cur, target)

        if opt == 0:
            opt = rotation
        else:
            if rotation < opt:
                opt = rotation

    return opt


A = [1, 6, 2, 3]

print(solution(A))


# [1, 2, 3]
# pip: 1 = > 2, pip: 2 = > 2 pip: 3 = > 2
