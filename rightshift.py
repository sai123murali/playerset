a,n=map(int,input().split())
li=list(map(int,input().split()[:a]))
li=(li[len(li)-n:len(li)]+li[0:len(li)-n])
for i in range(0,a):
    print(li[i],end=" ")