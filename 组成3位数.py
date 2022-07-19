import random
list=[]
len(list)<24 == True
while (len(list)<24):
    a=random.randint(1,4)
    b=random.randint(1,4)
    c=random.randint(1,4)
    d=(a,b,c)
    if d in list or a==b or a==c or b==c:
        pass
    else:
        list.append(d)
list.sort()
print(list)

