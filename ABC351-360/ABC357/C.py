n=int(input())
level_return=[['#']]
base = 1
ans = [['#' for _ in range(base)] for _ in range(base)]
for i in range(n):
    base = 3**(i+1)
    ans = [['' for _ in range(base)] for _ in range(base)]
    for x in range(base):
        for y in range(base):
            if x//(3**i)==1 and y//(3**i)==1:
                ans[x][y]='.'
            else:
                ans[x][y]=level_return[x%(3**i)][y%(3**i)]
    level_return = ans
for i in range(base):
    print(''.join(ans[i]))
