pin=input()
stack=[]
popen=["(","{","]"]
close=[")","}","]"]
def demo(pin):
    pos=0
    for i in range(len(pin)):
        if pin[i] in popen:
            stack.append(i)
            pos+=1
            continue
        if len(stack)==0:
            return pos+1
        temp=stack.pop()
        if temp=='(' and pin[i]==')' or temp=='[' and pin[i]==']' or temp=='{' and pin[i]=='}': 
            pos+=1
        else:
            return pos+1
    if len(stack)==0:
        return 0
    else:
        return pos+1
    
print(demo(pin))
    