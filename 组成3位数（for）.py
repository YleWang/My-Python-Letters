list=[]
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a!=b and b!=c and a!=c:
                d=(a,b,c)
                list.append(d)
print(list)