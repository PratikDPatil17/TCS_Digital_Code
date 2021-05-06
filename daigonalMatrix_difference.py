def digDiff(arr, n):
    s1 = 0
    s2 = 0
    for i in range(0,n):
        s1 = s1+arr[i][i]
        s2 = s2+arr[i][n-i-1]
    return abs(s1 - s2)

n = int(input())

arr = []

for i in range(0,n):
    arr.append(list(map(int, input().rstrip().split())))


result = digDiff(arr, n)
print(result)
