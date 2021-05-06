from itertools import combinations

def HSL(s):
    tgt = "HSL"
    str1 = ""
    str2 = ""
    arr = []
    arr2 = []
    count = 0
# Method 1 - using combinations function    
    l = list(map(list, combinations(s, 3)))
# Method 2 - using for loops to get all combinations
    for i in range(len(s)):
        str2 = ""
        for j in range(i,len(s)):
            for k in range(j, len(s)):
                str2 = s[i]+s[j]+s[k]
                if str2 == tgt:
                    arr2.append(str2)
    
    for i in l:
        str1 = "" 
        for j in i:
            str1 = str1+j
        arr.append(str1)
    print(arr)
    print(arr2)
    
    for i in arr:
        if i == tgt:
            count += 1
    return count
    for i in arr2:
        if i == tgt:
            count1 += 1

    return count1

s = "HHSL"
c1 = HSL(s)
print(c1)


#Method - 3
s = "HHSLHSL"
target = "HSL"
s1 = ""
arr = []
count =0
n = len(s)

for i in range(n):
    s1 = ""
    if s[i] == "H":
        for j in range(i,n):
            if s[j] == "S":
                for k in range (j,n):
                    if s[k] == "L":
                        count += 1   

print(count)

