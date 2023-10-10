def demo(s):
    l=[]
    for i in s:
        if i.isalpha():
            l.append(i)
        else:
            spc=i
            idxspc=s.index(i)
    l.reverse()
    l.insert(idxspc,spc)
    return "".join(l)


s=input()
print(demo(s))