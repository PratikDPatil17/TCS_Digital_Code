n= int(input())

if n<0 or n>1000000:
    print("Invalid input")
elif (n==0):
    print(9)

else:
    arr = []
    for i in range(10):
        arr.append(9-i)

    ans = 0
    tenth = 1

    while(n>0):
        digit = n%10
        replace = arr[digit]

        ans = ans + tenth*replace
        tenth = tenth*10
        n = n//10
    print(ans)

