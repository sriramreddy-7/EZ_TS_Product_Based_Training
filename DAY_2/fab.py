n=int(input("Enter the Number :"))
def fab(n):
    if n<=1:
        return n
    return fab(n-1)+fab(n-2)
for i in range(n):
    print(fab(i),end=",")

#0 1 1 2 3 5 8 13 21 34 