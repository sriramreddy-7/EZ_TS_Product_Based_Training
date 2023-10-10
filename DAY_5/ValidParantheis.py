l=input()
st=list(map(str,l))
p_open=['[','{','(']
p_close=[']','}',')']
stack=[]
if len(st)%2!=0:
    for i in st:
        if i==p_open[0]:
            stack.append(i)
            print("Invalid")
else:
    if st[0]==l[len(st)-1]:
        pass
    else:
        print("Invalid")