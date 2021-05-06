s = input()
t = input()


count = 0

for i in s:
    if i in t:
        for j in range(len(t)):
            if t[j] == i:
                t.replace(t[j],"@")
                break
    else:
        count+=1
print(count)
