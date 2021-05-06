def prod(n):
    product = 1
    while n>0:
        dig = n%10
        product = product*dig
        n = n//10

    return product

n = int(input())
print(prod(n))
