def saveThePrisoner(n,m,s):
    if (m+s-1) % n = 0:
        return n
    else:
        return (m+S-1)%n


t = int(input())
for i in range(t):
    n,m,s = map(int, input()rstrip().split())

    result = saveThePrisoner(n, m, s)
    print(result)
