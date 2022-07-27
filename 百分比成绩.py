a=input()
if str.isdigit(a) == True:
    a=int(a)
    if a/100>=0.9:
        print('您的成绩为A')
    elif a/100>=0.8:
        print('您的成绩为B')
    elif a/100>=0.7:
        print('您的成绩为C')
    elif a/100>=0.6:
        print('您的成绩为D')
    else:
        print('您的成绩为E')
else:
    print('您的成绩格式有问题')