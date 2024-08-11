n,t,a = map(int,input().split())
border = -(-n//2)
print('Yes' if t >= border or a >=border else 'No')