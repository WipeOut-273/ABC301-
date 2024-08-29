n,x,y,z=map(int,input().split())
if x>y:x,y=y,x
print('Yes' if x<z<y else 'No')