a = 1
b = 2
c = 3

def fn(c,d):
    e = 300
    #此时有几个局部变量???
    print('locals()返回:',locals())
    print("globals()返回:",globals())
    print(c)                #局部变量
    print(globals()['c'])   #全局变量
fn(100, 200)