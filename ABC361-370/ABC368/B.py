n=int(input())
A=list(map(int,input().split()))
cnt=0

def chk(Li):
    now=0
    for i in range(len(Li)):
        if Li[i]>0:
            now+=1
    return now>1

while chk(A):
    A = sorted(A, reverse=True)
    A[0]-=1
    A[1]-=1
    cnt+=1

print(cnt)