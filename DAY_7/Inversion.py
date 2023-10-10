l=list(map(int,input().split()))
count=0
for i in range(len(l)):
    k=i+1
    for j in range(k):
        if l[i]>l[j]:
            count+=1
            
print(count)
      