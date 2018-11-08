# 练习:
# 写一个函数hello,部分代码如下:
#     count = 0
#     def hello(name):
#         print("您好",name)
#         ...
#     当调用hello 函数时,全局变量count自动加1操作来记录hello被调用的次数
#      如:
#                 hello("To")
#                 hello("jerry")
#                 print("hello函数共被调用%d次" % count)

count = 0
def hello(name):
    global count
    print("您好",name)
    count +=1
    return count
hello("To")
hello("jerry")
print("hello函数共被调用%d次" % count)
