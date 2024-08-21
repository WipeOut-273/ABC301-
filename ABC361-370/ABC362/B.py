xa,ya = map(int,input().split())
xb,yb = map(int,input().split())
xc,yc = map(int,input().split())
point = [[xa,ya], [xb, yb],[xc, yc]]
L=[0,0,0]
for i in range(3):
    dist=0
    dist+=(point[i%3][0]-point[(i+1)%3][0])**2
    dist+=(point[i%3][1]-point[(i+1)%3][1])**2
    L[i]=dist
if sum(L)-max(L)*2==0:
    print('Yes')
else:
    print('No')