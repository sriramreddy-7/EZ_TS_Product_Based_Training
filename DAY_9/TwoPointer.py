l=list(map(int,input().split(',')))
target=int(input())
start=0
end=len(l)-1
l.sort()
for i in range(len(l)):
    if l[start]+l[end]>target:
        end=end-1
    if l[start]+l[end]<target:
        start=start+1
    if l[start]+l[end]==target:
        print(f"[{start+1},{end+1}]")
        break
   

