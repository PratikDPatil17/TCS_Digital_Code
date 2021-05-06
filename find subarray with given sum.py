arr = list(map(int, input().rstrip().split()))
findSum = int(input())

def getSubArray(arr, findSum):
    result = []
    for i in range(len(arr)):
        result.append(arr[i])

        while(sum(result)>findSum):
            result.pop(0)
        
        if (sum(result) == findSum):
            return result

    return []
