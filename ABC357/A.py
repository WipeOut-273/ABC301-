n,m=map(int,input().split())
A=list(map(int,input().split()))
hand=0
ans=0
for i in range(n):
    hand+=A[i]
    if hand<=m:
        ans+=1
print(ans)