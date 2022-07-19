list=[]
for iw in range(int(input('输入你的字符串有几位'))):
    sp=input('请输入你的第'+str(len(list)+1)+'个字符')
    if sp.isdigit() == True:pass
    else:list.append(sp)
print(list)
