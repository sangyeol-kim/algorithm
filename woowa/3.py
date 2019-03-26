

def rot13(para):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    capalphabet = "zyxwvutsrqponmlkjihgfedcba"
    #indexes = []
    result = ""
    for char in para:
        if ord('a') <= ord(char) <= ord('z'):
            index = ((ord(char)-ord('a')+13) % 26)
            result += alphabet[index]
        elif ord('A') <= ord(char) <= ord('z'):
            index = ((ord(char)-ord('A')+13) % 26)
            result += capalphabet[index]
        else:
            result += char
    return result


print rot13("hello my world")
