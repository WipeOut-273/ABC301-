n,k=map(int,input().split())
A=sorted(list(map(int,input().split())))
ans=float('inf')
for i in range(k+1):
    ans=min(ans, A[(n-k)+i-1]-A[i])
print(ans)