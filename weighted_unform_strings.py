def weightedUniformStrings(s, queries):
    result = []
    d = {}
    fc = s[0]
    currWeight = ord(fc) - 96
    d[fc] = currWeight
    for i in range(1,len(s)):
        if fc == s[i]:
            fc = s[i]
            d[fc] = currWeight
            currWeight += ord(fc)-96
            d[fc] = currWeight
            
        else:
            fc = s[i]
            currWeight = ord(fc)-96
            d[fc] = currWeight
    
    result = list(d.values())
    ans = []
    for i in queries:
        if i in result:
            ans.append("Yes")
        else:
            ans.append("No")
    return ans









