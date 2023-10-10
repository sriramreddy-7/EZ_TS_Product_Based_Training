def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

n = int(input())
li = list(map(int, input().split(',')))[:n]
li = bubble_sort(li)
for i in range(len(li)):
    if i != len(li)-1:
        print(li[i], end="->")
    else:
        print(li[i], end="")