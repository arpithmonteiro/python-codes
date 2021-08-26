l=[4,2,9,7,2,6,3]
for i in range(0,len(l)-1):
    min=i
    for j in range(i,len(l)):
        if l[j]<l[min]:
            min=j

    temp=l[i]
    l[i]=l[min]
    l[min]=temp

print(l)
