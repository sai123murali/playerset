a=list(input(""))
l=len(a)
for i in range(0,l,2):
    temp=a[i]
    a[i]=a[i+1]
    a[i+1]=temp
print("".join(a))