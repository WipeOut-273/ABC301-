s=input()
cnt=0
for i in range(len(s)):
    if s[-i-1]=='0':
        cnt+=1
    else:
        break
if cnt==0:
    print(s)
else:
    ans=s[:-cnt]
    print(ans if ans[-1]!='.' else ans[:-1])
        