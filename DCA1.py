s = input()
maxx = []
curr = [s[0]]

for i in range(len(s)):
    
    for j in range(i,len(s)):
        
        if s[j] not in curr:
            curr.append(s[j])
            
        else:
            if len(maxx)<len(curr):
                maxx = curr
                curr = []
                

print(maxx)

s1 = "".join(i for i in maxx)
print(len(s1))



#############################
# METHOD - 2
def maxUniqueSubArrayLen(s):
    map = {}
    if len(s) == 0:
        return 0
    max_length = start = 0

    for i in range(len(s)):
        if s[i] in map and start <=map[s[i]]:
            start = map[s[i]]+1
        else:
            max_length = max(max_length, i-start+1)
        map[s[i]] = i

    return (max_length)


res = maxUniqueSubArrayLen(s)
print(res)


