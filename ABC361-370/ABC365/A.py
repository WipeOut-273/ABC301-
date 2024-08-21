y = int(input())
flag1 = (y%4)!=0
flag2 = (y%4==0) and (y%100!=0)
flag3 = (y%100==0) and (y%400!=0)
flag4 = (y%400==0)

if flag4:
    print(366)
elif flag3:
    print(365)
elif flag2:
    print(366)
elif flag1:
    print(365)