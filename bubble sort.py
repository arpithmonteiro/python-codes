#bubblesort
l=[9,8,7,6,5,4]
for i in range(len(l)-1,0,-1):
    for j in range(i):
        temp=l[j]
        l[j]=l[j+1]
        l[j+1]=temp


print(l)
