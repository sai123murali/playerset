a1,b1=map(str,input().split())
c1=len(a1)
count=0
for i in range(c1):
    if(a1[i]!=b1[i]):
        count=count+1
if(count==1):
    print("yes")
else:
    print("no")
    