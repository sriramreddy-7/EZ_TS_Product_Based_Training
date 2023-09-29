"""Find out the smallest missing positive Integer
"""
size=int(input("Enter Size: "))
l=[]
m=[]
for i in range(0,size):
    l.append(int(input("Enter Element :")))
    if l[i]>=0:
        m.append(l[i]) 
max_e=max(m)
rn=[x for x in range(0,max_e+2)]
rn=set(rn)
m=set(m)
w=rn-m
w=list(w)
print(w)