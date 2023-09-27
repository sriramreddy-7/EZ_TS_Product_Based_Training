''''
x is having 100000 in bank account, rate of intrest is 12% per/Annum , 
in the 5th month x is withdrawing the 25000 in order oo buy gift 
for is loved one in the 9th month 10000 is deposited by 2nd loved one end of the finanacal 
year how much x is having in bank account.

prinicipal_amount=int(input("Principal Amount :"))
interest=int(input("Interest Rate :"))
transactions=int(input("Transcations:"))
ta=[],ma=[]
for i in range(0,transactions):
    x=int(input("Enter the Amount :"))
    y=int(input("Enter in which the month Amount is with drawn :"))
    ta.append(x)
    ma.append(y)
    x=0

def calculate():
    interest_amount=(prinicipal_amount*1*interest)/(100)
    month_wise=(interest_amount)/12

for i in range(0,transactions+1):
    calculate()
    prinicipal_amount-=ta[i]
    ta.pop()'''

prinicipal_amount=int(input("Principal Amount :"))
interest=int(input("Interest Rate :"))
transactions=int(input("Transcations:"))
ma=[]
for i in range(0,transactions):
    x=int(input("Enter the Amount :"))
    ma.append(x)
    x=0
for i in range(0,transactions):
    prinicipal_amount-=ma[i]
interest_amount=(prinicipal_amount*1*interest)/(100)
prinicipal_amount+=interest_amount    
print("prinicipal amount",prinicipal_amount)

