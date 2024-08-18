a,b,c=map(int,input().split())
ans='Yes'
while b!=c:
    if b==a:
        ans='No'
    b+=1
    b%=24
print(ans)
