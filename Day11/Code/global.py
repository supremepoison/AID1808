# 此示例示意Global语句的用法:

# v = 100
# def f1():
#     global v
#     v = 200

# f1()
# print('v=', v)

# #3.不能先声明局部变量,再用global声明为全局变量,此做法不符合规则
# v = 100
# def f1():
#     v = 200
#     global v

# f1()
# print('v=', v)

# 4.global变量列表里的变量名不能出现在函数的形参列表里

v = 100
def f1(v):
    global v
    v = 200
    print(v)

f1()
print('v=', v)#出错



