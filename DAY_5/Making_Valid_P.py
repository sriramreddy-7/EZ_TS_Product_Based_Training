l=input()
st=list(map(str,l))
p_open=['[','{','(']
p_close=[']','}',')']
stack=[]
if len(st)%2!=0:
    for i in st:
        if i==p_open[0]:
            stack.append(i)
            print("Invalid-1")
    else:
        stack.pop()
else:
    if st[0]==st[len(st)-1]:
        print("Valid")
    else:
        print("Invalid-2")
print(stack)