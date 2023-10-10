n=int(input())
arr=list(map(int,input().split(',')))
sum_array=sum(arr)
# print(f"Sum Array {sum_array}")
check=((n*(n+1))/2)-sum_array
print(int(check))
