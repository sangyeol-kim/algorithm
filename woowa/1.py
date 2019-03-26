# money = 50237
# lst = [0 for _ in range(10)]
# money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
# money = int(money)
# while (True):
#     if (money >= 50000):
#         lst[0] = money//50000
#         money %= 50000
#     elif(money < 50000 and money >= 10000):
#         lst[1] = money//10000
#         money %= 10000
#     elif(money < 10000 and money >= 5000):
#         lst[2] = money//5000
#         money %= 5000
#     elif(money < 5000 and money >= 1000):
#         lst[3] = money//1000
#         money %= 1000
#     elif(money < 1000 and money >= 500):
#         lst[4] = money//500
#         money %= 500
#     elif(money < 500 and money >= 100):
#         lst[5] = money//100
#         money %= 100
#     elif(money < 100 and money >= 50):
#         lst[6] = money//50
#         money %= 50
#     elif(money < 50 and money >= 10):
#         lst[7] = money//10
#         money %= 10
#     elif(money < 10 and money >= 1):
#         lst[8] = money
#         money = 0
#     if(money == 0):
#         break
# print(lst)


def solution(money):
    lst = []
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1]
    money = int(money)
    while (True):
        if (money >= 50000):
            lst[0] = money//50000
            money %= 50000
        elif(money < 50000 and money >= 10000):
            lst[1] = money//10000
            money %= 10000
        elif(money < 10000 and money >= 5000):
            lst[2] = money//5000
            money %= 5000
        elif(money < 5000 and money >= 1000):
            lst[3] = money//1000
            money %= 1000
        elif(money < 1000 and money >= 500):
            lst[4] = money//500
            money %= 500
        elif(money < 500 and money >= 100):
            lst[5] = money//100
            money %= 100
        elif(money < 100 and money >= 50):
            lst[6] = money//50
            money %= 50
        elif(money < 50 and money >= 10):
            lst[7] = money//10
            money %= 10
        elif(money < 10 and money >= 1):
            lst[8] = money
            money = 0
        if(money == 0):
            break

    return lst


solution(12345)
