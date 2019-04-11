string = "13+3*{24*(35-46.76)-89}"


def stringTokenizer(string, delimiter):

    result = []
    accu = ""
    for char in string:
        if char in delimiter:
            if accu != "":
                result.append(accu)
                accu = ""
            result.append(char)
        else:
            accu += char

    return result


result = stringTokenizer(string, "+-*/(){}[]^")
print(result)
