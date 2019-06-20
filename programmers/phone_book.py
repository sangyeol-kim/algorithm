def solution(phone_book):
    answer = True

    phone_book.sort()

    print(phone_book)

    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer = False
            return answer

    return answer


print(solution(["119", "97674223", "1195524421"]))
