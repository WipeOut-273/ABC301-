n,k=map(int,input().split())
R=list(map(int,input().split()))

def base_5(num):
    ret = ''
    while num:
        ret += str(num%5)
        num//=5
    return ret[::-1]

def plus1(Li):
    for i in range(len(Li)):
        Li[i]+=1
    return Li

ans=[]
for i in range(5**n):
    cnt=0
    now = list(map(int, base_5(i).zfill(n)))
    plus1(now)
    for j in range(n):
        if now[j]<=R[j]:
            cnt+=1
    if sum(now)%k==0 and cnt==n:
        ans.append(now)
for i in range(len(ans)):
    print(*ans[i])
