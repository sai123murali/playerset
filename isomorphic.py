a1,b1=map(str,input("").split())
if(len(a1)!=len(b1)):
    print("no")
else:
    c1=[a1.count(i)for i in a1]
    c2=[b1.count(i)for i in b1]
if(c1==c2):
    print("yes")
else:
    print("no")