import random
list=[]
while (len(list)<24):
    a=random.randint(1,4)
    b=random.randint(1,4)
    c=random.randint(1,4)
    d=(a,b,c)
    if d not in list and a!=b and a!=c and b!=c:list.append(d)
print(list)

