num = input()


def sumofsubs(num):
    n = len(num)
    sod = []
    sod.append(int(num[0]))
    result = sod[0]

    for i in range(1,n):
        numi = int(num[i])
        sod.append((i+1)*numi+10*sod[i-1])
        print(sod)
        result = result+sod[i]
        print("result = ",result)

    return result

print(sumofsubs(num))
    
