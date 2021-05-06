n = int(input())
arr = list(map(int, input().rstrip().split()))
s = []
for i in range(n):
    s.append(sum(arr[i+1:]))

print(s)
