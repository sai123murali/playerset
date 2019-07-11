p,q=map(int,input().split())
li=list(map(int,input().split()[:p]))
if q in li:
    print("Yes")
else:
    print("No")
