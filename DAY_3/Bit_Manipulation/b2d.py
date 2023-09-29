num=int(input())
pos=int(input())
bin_num=[]
def d2b(num):
    if num>1:
        d2b(num//2)
    bin_num.append(num%2)
d2b(num)
for i in range(len(bin_num)):
    if i==pos:
        if bin_num[i]==0:
            bin_num[i]=1
        else:
            bin_num[i]=0
l=[str(x) for x in bin_num]
st="".join(l)
print(int(st,2))
# print(bin(num).replace("0b",""))
