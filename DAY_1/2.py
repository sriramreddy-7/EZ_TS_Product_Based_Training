"""Get a num as input find the sum of the elements of number"""
num=int(input("Enter the Number : "))
k=num
sum=0
for i in str(num):
    sum=sum+int(i)
print("Sum of the Elements :",sum)

sum=0

while (num!=0):
    l=num%10
    sum=sum+l
    num=num//10
    
print("Sum of the Elements :",sum)

flag=len(str(k))
sum=0
for i in range(0,flag):
    x=k%10
    sum=sum+x
    k=k//10
print("Sum of the Elements :",sum)


    