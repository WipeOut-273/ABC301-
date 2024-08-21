h=int(input())
now=0
ans=0
while h >= now:
    now+=2**ans
    ans+=1
print(ans)
