n=int(input())
now=0
L=[[] for _ in range(n)]
for i in range(n):
    l,r=map(int,input().split())
    now+=l
    L[i]=[l,r]
if now>0:
    print('No')
else:
    ans=[L[i][0] for i in range(n)]
    for i in range(n):
        if now+(L[i][1]-L[i][0])<=0:
            now+=(L[i][1]-L[i][0])
            ans[i]=L[i][1]
        else:
            ans[i]=L[i][0]-now
            break
    if sum(ans)==0:
        print('Yes')
        print(*ans)
    else:
        print('No')