q=int(input())
ans=0
L = [0 for _ in range(10**6+1)]
for i in range(q):
    Q=list(map(int,input().split()))
    if Q[0]==1:
        if L[Q[1]]==0:
            ans+=1
        L[Q[1]]+=1

    elif Q[0]==2:
        L[Q[1]]-=1
        if L[Q[1]]==0:
            ans-=1
    
    elif Q[0]==3:
        print(ans)
    