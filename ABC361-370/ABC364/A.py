n=int(input())
ans='Yes'
now='salty'
flag = False
for i in range(n):
    s=input()
    if flag:
        ans = 'No'
    if now == 'sweet' and s=='sweet':
        flag = True
    now = s
print(ans)

