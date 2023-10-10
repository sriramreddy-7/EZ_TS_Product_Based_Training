n=int(input())
arr=list(map(int,input().split(',')))
res=0
for i in range(n):
    res=res^arr[i]
    if i!=n-1:
        res=res^arr[i-1]
print(res)