n=int(input())
l=[]
for i in str(n):
    l.append(int(i))
o=[]
for i in range(1,len(l),2):
        o.append(l[i])
print(o)
x=[str(x*x) for x in o]
print(x)
re="".join(x)
print(re[:4])
