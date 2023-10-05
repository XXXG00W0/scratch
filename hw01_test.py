
L = [1,7,2,7,3,7,4,7,5,7,6,7]
L = [3,3,1,1,1,3]
# L = [1,3,2,4,5,7,8,9,2,3,4]
def majority(L):
    c = 0
    v = L[0]
    cl = []
    vl = []
    for i in range(len(L)):
        if c == 0:
            v = L[i]
        if v == L[i]:
            c+=1
        else:
            c-=1
        cl.append(c)
        vl.append(v)
    print(c, v)
    print(L, '\n', cl, '\n', vl)
    c = 0
    cl = []
    for i in range(len(L)):
        if v == L[i]:
            c += 1
        else:
            c -= 1
        # cl.append(c)
    print(c, v)
    if abs(0 - c) == 0 - c:
        return False
    else:
        return True, v

print(majority(L))