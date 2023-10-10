oa=list(map(int,input().split(" "))) 
imp_l1=[0 for x in range(len(oa))]
qsum=[0 for x in range(len(oa))]
s=0
for i in range(len(oa)):
    imp_l1[oa[i]]=oa.count(oa[i])
# print(imp_l1)
for i in range(len(imp_l1)):
    s=s+imp_l1[i] 
    qsum[i]=s
# print(qsum)
result=[0 for x in range(len(oa))]
for i in range(1,len(oa)+1):
    key=oa[len(oa)-i]
    # print(f"Key is ={key}")
    qsum[key]=qsum[key]-1
    # print(f"r = {qsum[key]}")
    result[qsum[key]]=key
    # print(f"result[{qsum[key]}]={result[qsum[key]]}")
    # print(result)
    # print("")
print(result)