"""
Swap two Numbers using the XOR Operation
"""
num1=int(input("Enter the Num 1: "))
num2=int(input("Enter the Num 2: "))
print("Num-1",num1,"Num2",num2)
num1=num1^num2 
num2=num1^num2
num1=num1^num2
print("Num-1",num1,"Num2",num2)