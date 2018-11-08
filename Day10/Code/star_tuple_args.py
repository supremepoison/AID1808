# 此示例示意星号元祖形参的定义及使用

# def func(*args):
#     print("用户传入的参数个数是:", len(args))
#     print('args=', args)
# func()
# func(1,2,3)
# func(1,2,3,4,'a','b','c')

def fun(*args):
    print(args)
fun(1,2,3.2,'ssssss')