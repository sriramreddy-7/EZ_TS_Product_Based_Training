l=int(input("Enter the l :"))
r=int(input("Enter the R :"))
xor=0
for i in range(l,r+1):
    xor=xor^i
print(xor)