def solution(phone_book):
    answer = True

    temp = ''

    for i in phone_book:
        if (len(phone_book[i]) < len(phone_book[1])):
            temp = phone_book[i]

    print(temp)


phone = ["119", "97674223", "1195524421"]

solution(phone)
