l=list(map(str,input().split(',')))
op=""
for i in l:
    nc=i.split(':')
    name=nc[0]
    code=nc[1]
    max=0
    for i in code:
        if int(i) and int(i)<=len(name):
            max=int(i)
    if max==0:
        op+='X'
    else:
        op+=name[max-1]
print(op)

