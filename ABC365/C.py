n,m=map(int,input().split())
A=sorted(list(map(int,input().split())))

def is_ok(mid):
    Sum = 0
    for i in range(n):
        Sum += min(A[i], mid)
    return Sum <= m

def meguru_bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok+ng)//2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = meguru_bisect(10**9+1, 0)
print(ans if sum(A) > m else 'infinite')