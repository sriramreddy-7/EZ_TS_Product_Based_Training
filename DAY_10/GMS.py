def gms():
    for row in arr:
        if sum(row) != 15:
            return False
    for i in range(len(arr)):
        temp = 0
        for j in range(len(arr)):
            temp += arr[j][i]
        if temp != 15:
            return False
        
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                temp += arr[i][j]
    if temp != 15:
        return False
    
    i=0, j=n-1
    while i < n and j >=0:
        temp += arr[i][j]
        i += 1
        j -= 1
    if temp != 15:
        return False
 
print(gms())