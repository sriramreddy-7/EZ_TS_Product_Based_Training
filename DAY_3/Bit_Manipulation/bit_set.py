'''num=int(input())
pos=int(input())
bin_num=[]
def d2b(num):
    if num>1:
        d2b(num//2)
    bin_num.append(num%2)
d2b(num)
for i in range(len(bin_num)):
    if i==pos:
        if bin_num[i]==1:
            print("Set")
        else:
            print("No")'''

"""
num=int(input())
k=int(input())
if num &(1<<k-1):
    print("Set")
else:
    print("No")
    """