list=[]
for i in range(int(input('输入你的字符串有几位'))):
    s=input('请输入你的第'+str(len(list)+1)+'个数')
    if s.islower() == True:s=s.upper()
    list.append(s)
print(list)