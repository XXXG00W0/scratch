# hanoi_tower
count = 0

def printf(origin, destination):
    global count
    count+=1
    print("Move the top dish from rod", origin, "to rod", destination)

def move(n, start, end):
    rods = [1, 2, 3]
    rods.remove(start)
    rods.remove(end)
    transfer = rods[0]
    if n == 1:
        printf(start, end)
    else:
        move(n-1, start, transfer)
        move(1, start, end)
        move(n-1, transfer, end)
    
move(6,1,3)
print(count)