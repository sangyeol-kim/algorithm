n = int(input())

if (n >= 1 and n <= 100):
    for i in range(1, n+1):
        print(" "*(i-1) + "*"*((2*n)-(2*i-1)))
    for j in range(1, n):
        print(" "*(n-j-1) + "*"*(2*j+1))
