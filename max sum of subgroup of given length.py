s = input()
n = int(input())
output = [(s[i:i+n]) for i in range(0, len(s), n)]

maxsum = cur = 0
k = []
for i in range(0,len(s),n):
    k.append(s[i:i+n])
for i in k:
    cur = 0
    for j in range(len(i)):
        cur = cur + int(i[j])
    maxsum = max(cur, maxsum)
print(k,maxsum)
print(output)
