def pyramid(n):
    for i in range(1,n+1):
        
        if i > 1 and i%2!=0:
            s = ("#"*i)*2
        elif i == 1:
            s = "#"*i
        else:
            pass
        
        print(s.center(n))
pyramid(5)
