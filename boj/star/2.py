
n = int(input())

if (n >= 1 and n <= 100):
    for i in range(1, n+1):
        print(" "*(n-i) + "*"*i)
