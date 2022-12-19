def election(x,y,z):
    sum = x+y+z
    return 1 if sum>=2 else 0

a = input().split()
print(int(election(int(a[0]),int(a[1]),int(a[2]))))