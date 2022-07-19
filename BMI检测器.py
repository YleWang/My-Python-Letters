a=int(input('输入你的体重（kg）'))
b=int(input('输入你的身高（cm）'))
sum=a/b/b*10000
if sum<18.5:print('您属于过轻')
elif sum<25:print('您属于正常')
elif sum<28:print('您属于过重')
elif sum<32:print('您属于肥胖')
else:print('您属于严重肥胖')
