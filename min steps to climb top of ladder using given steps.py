arr = [1,3,5, 3, 8, 2, 6, 7, 6, 8, 9]

a = len(arr)
step = 0
count = 0
summ = 0
while(a>summ):
    summ = summ+arr[step]
    print("sum = ",summ)
    step = step+arr[step]
    print("step = ",step)
    count+=1

print(count)
