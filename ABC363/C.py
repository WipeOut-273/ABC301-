from more_itertools import distinct_permutations

n,k=map(int,input().split())
S=list(input())

c = distinct_permutations(S)
ans=0
for v in c:
    for i in range(n-k+1):
        if v[i:i+k]==v[i:i+k][::-1]:
            break
    else:
        ans+=1
print(ans)
