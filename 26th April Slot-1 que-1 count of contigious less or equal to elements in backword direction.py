n = int(input())
arr = list(map(int, input().rstrip().split()))


for i in range(n):
    count = 0
    
    for j in arr[i::-1]:
        # print(arr[i]," - ",j)
        if arr[i] >= j:
            count += 1
        else:
            break

    print(arr[i]," - ",count)
