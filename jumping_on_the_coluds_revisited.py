def jumpingOnClouds(c,k):
    e = 100
    i = 0

    while True:
        e = e - 1 - 2 * c[i]
        i = (i+k) % n

        if i == 0:
            break
    return e


n,k = map(int, input().split())
c = list(map(int, input().rstrip().split()))


r = jumpingOnClouds(c, k)
print(r)
