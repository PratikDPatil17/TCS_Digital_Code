s1 = input()
s2 = input()
ans = ""

ss1 = []
ss2 = []
res = []

for i in range(0,len(s1),2):
    ss1.append(s1[i:i+2])
for j in range(0,len(s2),2):
    ss2.append(s2[j:j+2])


for i in range(len(ss1)):
    for j in range(len(ss2)):
        if i == j:
            res.append(ss1[i]+ss2[j])
            print

    
    
for i in range(len(res)):
    ans = ans+res[i]


print(ans)
    
