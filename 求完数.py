list=[]
for i in range(999):
    i,p=i+1,0
    for b in range(1,1000):
        if i%b ==0:
            p+=b
    if p==2*i:
        list.append(i)
print('完数是',list)

# for i in range(999):
#     list = []
#     for t in range(1,i):
#         if i%t==0:
#             list.append(t)
#     if sum(list)==i:
#         print(list,'完数是',sum(list))