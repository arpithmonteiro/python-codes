#insertionsort
list=[5,3,6,2,1]
for i in range(1,len(list)):
    temp=list[i]
    j=i-1
    while j>=0 and list[j]>temp:
        list[j+1]=list[j]
        j-=1
    list[j+1]=temp
print(list)
