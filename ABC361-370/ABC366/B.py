n=int(input())
maxlen=0
S=['' for _ in range(n)]
for i in range(n):
    S[i]=input()
    maxlen=max(maxlen, len(S[i]))
for i in range(n):
    S[i]+='*'*(maxlen-len(S[i]))

ans = ['' for _ in range(maxlen)]
for i in range(maxlen):
    for j in range(n):
        ans[i]+=S[j][i]
for i in range(maxlen):
    ans[i]=ans[i][::-1].rstrip('*')
    print(ans[i])

