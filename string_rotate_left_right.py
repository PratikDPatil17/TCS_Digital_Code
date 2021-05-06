def rotate(s,d):
    left= s[d:]+s[:d]
    right = s[len(s)-d:]+s[:len(s)-d]

    print("right = ",right)
    print("left = ",left)
    if right==left:
        return 1
    else:
        return 0

s = input()
d = int(input())

res = rotate(s,d)
print(res)
