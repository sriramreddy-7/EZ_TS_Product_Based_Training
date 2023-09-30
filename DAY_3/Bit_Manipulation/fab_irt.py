n=int(input("Enter the Number :"))
def fab(n):
    if n<=1:
        return n
    return fab(n-1)+fab(n-2)
for i in range(n):
    print(fab(i),end=",")