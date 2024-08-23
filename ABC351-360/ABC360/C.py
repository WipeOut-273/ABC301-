n=int(input())
A=list(map(int,input().split()))
W=list(map(int,input().split()))
now = [0 for _ in range(n)]
ans=0
for i in range(n):
    if now[A[i]-1]<W[i]:
        ans+=now[A[i]-1]
        now[A[i]-1]=W[i]
    else:
        ans+=W[i]
print(ans)
