
class A:
    def __init__(self):
        self.st = input("Enter the String: ")
        self.num1 = int(input("Enter the Num 1: "))
        self.num2 = int(input("Enter the Num 2: "))
    def findSq(self):
        print("Reverse",self.st,self.st[::-1])
        print("Square",self.num1 ,self.num1**2)
    def value(self):
        print("String Length",len(self.st))
        print("Modulo Division",self.num1 % self.num2)

obj = A()
obj.findSq()
obj.value()