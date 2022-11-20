n = int(input())
ans = n * 45 + (n // 2)*5 + ((n+1)//2-1)*15
print(ans//60 + 9, ans%60)