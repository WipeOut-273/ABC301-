n,k=map(int,input().split())
A=list(map(int,input().split()))
ans=[]
for i in range(k):
    ans.append(A[-i-1])
ans=ans[::-1]
print(*(ans+A[:n-k]))
