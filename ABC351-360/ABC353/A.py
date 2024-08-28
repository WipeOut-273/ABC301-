n=int(input())
H=list(map(int,input().split()))
h = H[0]
ans=-1
for i in range(n):
    if h<H[i]:
        ans=i+1
        break
print(ans)
