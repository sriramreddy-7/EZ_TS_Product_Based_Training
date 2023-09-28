size=int(input("Enter the Size :"))
l=[]
def array_sum(size):
    sum=0
    for i in range(size):
        l.append(int(input()))
        sum=sum+l[i]
    return sum
print("Sum is",array_sum(size))

    