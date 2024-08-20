n,x,y=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
AB=[[A[i],B[i]] for i in range(n)]
AB_x=sorted(AB, key=lambda a:a[0], reverse=True)
AB_y=sorted(AB, key=lambda a:a[1], reverse=True)

now_xx, now_xy, now_yx, now_yy = 0, 0, 0, 0
ans=n
for i in range(n):
    now_xx+=AB_x[i][0]
    now_xy+=AB_x[i][1]
    if now_xx>x or now_xy>y:
        ans=i+1
        break

for i in range(n):
    now_yx+=AB_y[i][0]
    now_yy+=AB_y[i][1]
    if now_yx>x or now_yy>y:
        ans=min(ans, i+1)
        break

print(ans)