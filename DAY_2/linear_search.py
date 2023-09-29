size=int(input("Enter the Size :"))
l=[]
for i in range(size):
    l.append(int(input()))
key=int(input("Enter the Search Element : "))
def search(key):
    for i in range(len(l)):
        if key==l[i]:
            return 1
r=search(key)      
if r==0:
    print("Element is not found")
else:
    print("Element is found",l.index(key),"Position")
    
