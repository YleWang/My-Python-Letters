l=int(input('你想玩几局'))
f=l
sum=0
e=0
while l>0:
                a=int(input('输入你的出牌，0是剪刀，1是石头，2是布'))
                import random
                s=int(random.randint(0,2))
                if a>s:
                                if a==2 and s==0:print('好遗憾，你输了')
                                else:
                                                print('恭喜你，你赢了')
                                                sum=sum+1
                                                e=e+1
                                
                elif a==s:
                                print('平局，再来一次吧')
                                l=l+1
                elif a<s:
                                if a==0 and s==2:print('恭喜你，你赢了')
                                else:
                                                print('好遗憾，你输了')
                                                sum=sum-1
                print('你的出牌是‘',a,'’机器的出牌是‘',s,'’')
                l=l-1
                print('            ')
if 2*sum>f:print('你赢了',e,'局，恭喜你获得胜利')
elif 2*sum<f:print('你赢了',e,'局，很遗憾你输了')
else:print('平局哦，再玩一次吧')
