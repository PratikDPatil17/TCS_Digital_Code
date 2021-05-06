n = int(input())

if n%2 == 0:
    num = n//2
    print(n-1)
elif n%2 != 0:
    num = (n//2)+1
    print(n-3)
