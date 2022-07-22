import math
x=int(input('输入x：'))
if x<-10:y=abs(x)+5
elif abs(x)<10:y=4*(x-2)
elif x>10:
    y=round(math.sqrt(x),2)
print(y)