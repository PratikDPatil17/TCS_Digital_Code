def countDivisor(n):
    m = n
    count = 0

    while n > 0:
        dig = n%10
        if dig == 0:
            pass
        else:
            if m % dig == 0:
                count = count+1
            else:
                pass

        n = n//10

    return count

t = int(input())
for i in range(t):
    n = int(input())
    result= countDivisor(n)
    print(result)
