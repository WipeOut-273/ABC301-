n,t,p=map(int,input().split())
L=list(map(int,input().split()))

def chk(Li,border):
    cnt=0
    for i in range(len(Li)):
        if Li[i]>=border:
            cnt+=1
    return cnt
def plus_one(Li):
    for i in range(len(Li)):
        Li[i]+=1
    return Li

ans=0
while chk(L, t)<p:
    plus_one(L)
    ans+=1
print(ans)
