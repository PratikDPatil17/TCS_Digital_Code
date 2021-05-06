arr = []

n = int(input())

if n<= 100:
    for i in range(n):
        arr.append(int(input()))

    count_0 = 0
    count_1 = 0
    count_2 = 0

    for i in range(n):
        if arr[i] == 0:
            count_0 += 1
        if arr[i] == 1:
            count_1 += 1
        if arr[i] == 2:
            count_2 += 1

    for i in range(count_1):
        print("1", end=" ")
    for i in range(count_0):
        print("0", end=" ")
    for i in range(count_2):
        print("2", end=" ")
    
else:
    print("Invalid Input")


