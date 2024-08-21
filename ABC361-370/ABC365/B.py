n = int(input())
A = list(map(int,input().split()))
maxA = max(A)
index = 0
secondBest = 0
for i in range(n):
    if A[i]!=maxA:
        if secondBest < A[i]:
            index = i+1
            secondBest = A[i]
print(index)
