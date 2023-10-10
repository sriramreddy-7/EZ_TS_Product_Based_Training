num=int(input())
pos=int(input())
bin_num=[]
def d2b(num):
    if num>1:
        d2b(num//2)
    bin_num.append(num%2)
d2b(num)
print(bin_num)
for i in range(1,len(bin_num)+1):
    if i==pos-1:
        if bin_num[i]==1:
            bin_num[i]=0
        else:
            bin_num[i]=1
m=[str(x) for x in bin_num]
re="".join(m)
print(re)
print(int(re,2))

"""
num=int(input())
k=int(input())
if num &(1<<k-1):
    print("Set")
else:
    print("No")
    """