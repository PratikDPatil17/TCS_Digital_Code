arr = list(map(int, input().rstrip().split()))
n = int(input())

def maxSumOfGivenLength(arr,n):
    res = arr[:n]
    maxsum = currsum = sum(res)

    for i in range(n, len(arr)):
        
        if arr[i] > min(res):
        
            res.remove(min(res))
            
            res.append(arr[i])
            print(res)
            
            currsum = sum(res)
        else:
            currsum = currsum

        maxsum = max(currsum, maxsum)
    return maxsum

rs = maxSumOfGivenLength(arr,n)
print(rs)
        
