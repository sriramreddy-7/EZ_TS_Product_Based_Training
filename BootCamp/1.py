"""
Create one class , class consist of three variables
take 2 methods 
2 argumented fun
1-string 2-int argument
in side the method print the string reverse
print the square of integer argument value.

2nd method in the class method name is display_result
inside of method find the length of a string.
and 
print the modulo division of 2 integer variables
pass run time 
"""

class A:
    def __init__(self,x,y,z):
        self.x=str(x)
        self.y=int(y)
        self.z=int(z)
    
    def findSq(self):
        print("Square",self.x**2)
        print("Square",self.y**2)
        
    def value(self):
        print(len(self.x))
        print(self.y//self.z)
    
st=input("Enter the String :")
x=int(input("Enter the Num 1: "))
y=int(input("Enter the Num 2: "))
obj=A(st,x,y)
obj.findSq()
obj.value()
'''obj.findSq(num1,num2)
obj.value(st,num1,num2)'''
