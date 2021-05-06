def climbing(a, b):
    a = sorted(list(set(a)), reverse = True)
    #b.sort(reverse = True)

    j = 0
    l = len(a)

    result = []
    

    for i in range (len(b)):
        while j < l and b[i] < a[j]:
            j = j+1
            continue
        result.append(j+1)

    return result



n = int(input())
scores = list(map(int, input().rstrip().split()))
m = int(input())
chacha = list(map(int, input().rstrip().split()))

result = climbing(scores, chacha)

print(result)

