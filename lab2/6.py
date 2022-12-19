a = input().split()

def power(a,n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        ans = a
        for i in range(1,n):
            ans *= a
        return ans



print(power(float(a[0]),int(a[1])))