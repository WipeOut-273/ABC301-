def chk(x11,x12,x21,x22):
    return not(x12 <= x21 or x22 <= x11)


a,b,c,d,e,f = map(int,input().split())
g,h,i,j,k,l = map(int,input().split())

if chk(a,d,g,j) and chk(b,e,h,k) and chk(c,f,i,l):
    print('Yes')
else:
    print('No')