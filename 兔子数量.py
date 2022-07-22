#a=上一次,b=这一次
a,b,list= 0,1,[]
for i in range(12):
    list.append(b)
    a,b=b,a+b
print(list[-1])

