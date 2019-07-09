inp=str(input())
max=0
for i in inp:
    if(inp.count(i)>max):
        max=inp.count(i)
        mi=i
print(mi)