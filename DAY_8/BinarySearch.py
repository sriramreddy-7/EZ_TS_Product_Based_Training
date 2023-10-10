l=list(map(int,input().split(" ")))
key=int(input("Enter the Key: "))
l.sort()
start=0
end=len(l)-1
mid=(start+end)//2
print(mid)
flag=0
def bs(start,end,l):
    if (key==l[mid]):
        print("Ele Found")
        flag=1 
    elif(key<l[mid]):
        return bs(start,mid,l)
    else:
        return bs(mid+1,end,l)         
    
bs(start,end,l)
if flag==1:
    print("not found")