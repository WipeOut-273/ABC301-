n=int(input())
H=list(map(int,input().split()))
sub=[1,1,3]
ans=0
for i in range(n):
    ans+=(H[i]//5)*3
    now=H[i]%5
    while now>0:
        ans+=1
        if ans%3:
            now-=1
        else:
            now-=3
print(ans)