n = int(input())
ans = 0
d = 0
while(n>0):
    a=n%10
    ans += a*(2**d)
    d+=1
    n//=10

print(ans)