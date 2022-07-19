a=int(input('输入a:'))
b=int(input('输入b（与a要间隔10以上哦）:'))
if a-b>10 or b-a>10:
               
                import random
                s=random.randint(a,b)
                print('猜猜我心里有几个王心凌','(',a,'到',b,')')
                g=0
                t=10
                while(g!=s)and(t>0):
                                g=int(input())
                                t=t-1
                                if g==s:print('爱你，爱你')
                                elif g>s:print('多了一点')
                                else:print('少了一点')
                                if t>0:print('常常说你猜的数是不是不太对呀')
                                elif t<0:print('不爱你，不爱你')
else:print('a和b要间隔10以上哦')
                                                                                
