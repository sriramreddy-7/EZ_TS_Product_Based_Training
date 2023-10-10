def demo(s):
    Number1=0
    f4=s.index(4)
    s7=s.index(7)
    for i in range(0,f4):
        Number1=Number1+s[i]
    for j in range(s7+1,len(s)):
        Number1=Number1+s[j]
    print(Number1)
    l=[]
    for i in range(f4,s7+1):
        l.append(str(s[i]))
    Number2="".join(l)
    return Number1+int(Number2)
    
s=list(map(int,input().split(',')))
if __name__=="__main__":
    print(demo(s))
        


