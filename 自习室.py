l=0
import random
x=int(input('欢迎来到自习室，你想做几道题？'))
if x>4:
                for i in range(x):
                                a=random.randint(100,1000)
                                b=random.randint(100,1000)
                                c=a+b
                                print(a,'+',b)
                                sum=int(input())
                                if sum==c:l+=1
                if l==x:print('全对啦恭喜你')
                else:print('本次您答对了',l,'题')
else:print('最少要做5题哟！')
