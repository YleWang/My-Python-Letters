x=int(input('输入第一个数'))
y=int(input('输入第二个数'))
z=int(input('输入第三个数'))
if x==y or y==z or x==z:print('三个数不能一样哦')
else:
                if x>y and y>z:print(x,y,z)
                elif x>y and z>y:
                                if x>z:print(x,z,y)
                                elif z>x:print(z,x,y)
                elif y>z and z>x:print(y,z,x)               
                elif y>z and x>z:
                                if x>y:print(x,y,z)
                                elif y>x:print(y,x,z)
                elif z>x and x>y:print(z,x,y)
                elif z>x and y>x:
                                if z>y:print(z,y,x)
                                elif y>z:print(y,z,x)
