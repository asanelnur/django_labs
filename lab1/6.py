a = int(input())
b = int(input())
c = int(input())
if a>=b:
    if a>c:
        print(a)
    else:
        print(c)
elif b>=a:
    if b>c:
        print(b)
    else:
        print(c)
else:
    print(c)