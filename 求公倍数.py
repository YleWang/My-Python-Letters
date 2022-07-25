i=int(input('输入第一个数'))
t=int(input('输入第二个数'))
list_1,list_2,list_3=[],[],[]
for a in range(2,i):
    if i%a == 0:
        list_1.append(a)
for b in range(2,i):
    if t%b == 0:
        list_2.append(b)
s=len(list_1)
for k in range(s):
    if list_1[k] in list_2:
        list_3.append(list_1[k])
w=len(list_3)
if w==0:
    sum=i*t
else:
    for y in range(w):
        sum=i*t/list_3[y]

print(sum)
