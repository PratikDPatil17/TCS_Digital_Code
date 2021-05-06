n = int(input())
def rev(num):
    temp = num
    rev = 0
    if n==0:
        return temp

    while(num>0):
        dig = num%10
        rev = rev*10+dig
        num = num//10

    if rev == temp:
        return True
    else:
        return False

print(rev(n))
