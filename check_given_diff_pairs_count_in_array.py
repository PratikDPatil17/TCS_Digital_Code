def pairs(k, arr):
    arr = set(arr)
    return sum(1 for i in arr if i+k in arr)
        

def pairs2(k, arr):
    q = 0
    n = len(arr)
    arr = set(arr)
    h = len(arr) - n

    for i in arr:
        if i+k in arr:
            q = q+1
    return q+h

n , k = map(int, input().split())
arr = list(map(int, input().rstrip().split()))
count = pairs(k, arr)
print(count)




