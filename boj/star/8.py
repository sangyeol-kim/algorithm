n = int(input())

if (n >= 1 and n <= 100):
    for i in range(1, n+1):
        print("*"*i + " "*((2*n)-(2*i)) + "*"*i)
    for j in range(1, n):
        print("*"*(n-j) + " "*(2*j) + "*"*(n-j))
