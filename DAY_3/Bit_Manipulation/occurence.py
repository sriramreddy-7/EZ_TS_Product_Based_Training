"""
In given array every no occurs only one numbers occurs 1 time
find the element that occurs only once.
"""
size=int(input("Enter the Size :"))
array=[]
for i in range(size):
    array.append(int(input()))
def find(array,n):
    res=array[0]
    for i in range(1,n):
        res=res^array[i]
    return res 
print("Element is:",find(array,size))