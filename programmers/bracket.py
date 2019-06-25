def solution(s):
    answer = True

    stack = []

    for i in s:
        if s[0] == ")":
            answer = False
            break
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                answer = False
                break
            else:
                stack.pop()

    if len(stack) != 0:
        answer = False

    return answer
