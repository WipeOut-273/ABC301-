L=[]
for i in range(1,350):
    if i!=316:
        L.append('ABC'+str(i).zfill(3))
print('Yes' if input() in L else 'No')