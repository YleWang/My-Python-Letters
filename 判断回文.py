ass=str(input('输入你的数'))
if ass!=ass[::-1]:print('你输入的不是回文')
else:print('你输入的是回文')

# a=int(input('输入你的数有几位(大于2位)'))
# count=0
# time=-1
# time_2=0
# list=[]
# u=0
# for i in range(a):
#     count+=1
#     g=('请输入你的第'+count+'个数')
#     s=int(input(g))
#     list.append(s)
# b=int(len(list)/2)
# if b%2>=1:b+=0.5
# for i in range(b-1):
#     time=time+1
#     time_2=time_2-1
#     if list[time] != list[time_2]:
#         u=u+1
#         break
#     else:pass
#
# if u>=1:print('你的数不是回文')
# else:print('你的数是回文')