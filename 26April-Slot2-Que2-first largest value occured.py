n = int(input())
arr = list(map(int, input().rstrip().split()))
currMax = arr[0]
for i in range(1,n):
    if currMax < arr[i]:
        currMax = arr[i]
    else:
        break
print(currMax)
    
