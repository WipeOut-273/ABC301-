n,k,x=map(int,input().split())
A=list(map(int,input().split()))
B=[]
for i in range(n):
    B.append(A[i])
    if i==k-1:
        B.append(x)
print(*B)