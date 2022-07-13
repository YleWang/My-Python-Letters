a=72
b=85
sum=((b-a)/a*100)
if sum%0.1>=0.5:
    e=sum//0.1/10+0.1
else:e=sum//0.1/10
print('小明的成绩提升了',e,'%')