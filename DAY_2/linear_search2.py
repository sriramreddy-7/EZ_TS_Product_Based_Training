size=int(input("Enter the Size :"))
l=[]
for i in range(size):
    l.append(int(input()))
key=int(input("Enter the Search Element :"))
if l.index(key)==True:
    print("Element is Found")
else:
    print("Element is Not Found")