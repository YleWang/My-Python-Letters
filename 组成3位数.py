import random
list=[]
len(list)<64 == True
while (len(list)<64):
    a=random.randint(1,4)
    b=random.randint(1,4)
    c=random.randint(1,4)
    d=(a,b,c)
    if d in list:
        pass
    else:
        list.append(d)
list.sort()
print(list)

