start=int(input("Start at :"))
end=int(input("End at :"))
size=int(input("Enter the Range :"))
l=[]
while len(l)!=size:
    x=int(input("Enter the Number :"))
    if x >=start and x<=end:
            l.append(x)
    else:
        print("Not in the Range")
lmax=max(l)
print("Even No :")
for i in l:
    if i%2==0:
        print(i)
print("Powers :\n")
for i in range(0,lmax+1):
    if 2**i in l:
        print(2**i)


    
