h,w=map(int,input().split())

x,y=map(int,input().split())
x-=1
y-=1

M = {'U':[-1,0], 'D':[1,0], 'L':[0,-1], 'R':[0,1]}

C=[list(input()) for _ in range(h)]

s=input()
for i in range(len(s)):
    move = M[s[i]]
    xx = x + move[0]
    yy = y + move[1]
    if 0<=xx<h and 0<=yy<w:
        if C[xx][yy]!='#':
            x = xx
            y = yy
x+=1
y+=1
print(x, y)
