a1,b1=map(int,input("").split())
li=list(map(str,input("").split()))
li.sort(reverse=True)
print(li[b1-1])
