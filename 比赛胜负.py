a,b,c,d=int(input('获取A队分数')),int(input('获取B队分数')),int(input('目前是谁控球？A队输入‘1’，B队输入‘2’')),int(input('输入剩余时间'))
sum=abs(a-b)-3
if sum>=0.5:
    if a>b and c==1:sum+=0.5
    elif a>b and c==2:sum-=0.5
    elif a<b and c==1:sum-=0.5
    else:sum+=0.5
elif (a>b and c==1) or (a<b and c==2):sum+=0.5
elif a==b:sum=0
sum=sum**2
if sum>d:print('领先队伍是安全的')
else:print('领先队伍是安全的')