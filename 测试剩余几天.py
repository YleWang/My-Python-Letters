a=int(input('你的账号有计划几个硬币呀？'))
b=int(input('你现在有多少经验'))
sum=28800-b
c=a//4
d=a%4
if d>0:
    l=c+(sum-65*c-10*d-25)/25
else:
    l=c+(sum-65*c)/25
if l%10>0:
    e=l//10*10
else:e=l
print('你最快还需要大约',int(e),'天就可以到达LV6了')
