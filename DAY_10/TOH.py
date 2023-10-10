'''def TOH(n, src, aux, dest):
    if n <= 1:
        print(src + " -> " + dest)
        return
    TOH(n-1, 'src', 'dest', 'aux')
    print(src + " -> " + dest)
    TOH(n-1, 'aux', 'src', 'dest')
n = 4
TOH(n, 'src', 'aux', 'dest')'''
def count(n):
    if n == 1:
        return 1 
    return 2*count(n-1)+1
    
n=2    
ans = count(3)
print(ans)
print((2**n) - 1)