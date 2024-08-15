n,l,r =map(int,input().split())
ans = [i+1 for i in range(n)]
ans[l-1:r] = ans[l-1:r][::-1]
print(*ans)