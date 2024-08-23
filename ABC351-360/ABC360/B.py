s,t=map(str,input().split())
ans='No'
for i in range(len(s)-1):
    li = ['' for _ in range(i+1)]
    for j in range(len(s)):
        li[j%(i+1)]+=s[j]
    if t in li:
        ans='Yes'
print(ans)