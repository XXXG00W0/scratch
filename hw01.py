
def f():
    L = [1, 1, 1, 1, 2, 3, 4, 5, 5, 1, 1, 1, 5]
    c = 0
    v = L[0]
    for i in range(len(L)):
        if c == 0:
            v = L[i]
        if v == L[i]:
            c += 1
        else:
            c -= 1
    print(L, c, v)
    c = 0
    # v = L[0]
    for i in range(len(L)):
        if v == L[i]:
            c += 1
        else:
            c -= 1
    print(L, c, v)
    if c <= 0:
        return False
    else:
        return v
    
print(f())