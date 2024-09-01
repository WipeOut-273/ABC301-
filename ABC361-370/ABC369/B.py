n=int(input())
L=[]
R=[]
for i in range(n):
    a,s=input().split()
    if s=='L':
        L.append(int(a))
    elif s=='R':
        R.append(int(a))
ans=0
for i in range(len(L)-1):
    ans+=abs(L[i+1]-L[i])
for i in range(len(R)-1):
    ans+=abs(R[i+1]-R[i])
print(ans)