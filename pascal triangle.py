n=int(input("how many rows do you want? "))
a=[]
for j in range(n):
    a.append([])
    a[j].append(1)
    for k in range(1,j):
        a[j].append(a[j-1][k-1]+a[j-1][k])
    if(n!=0):
        a[j].append(1)
for j in range(n):
    print("   "*(n-j),end=" ",sep=" ")
    for k in range(0,j+1):
        print('{0:6}'.format(a[j][k]),end=" ",sep=" ")
    print()
