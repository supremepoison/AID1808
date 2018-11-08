
# 此示例示意pyth的作用域

# v = 100         #G
# def f1():
#     v = 200     #E
#     print('f1.v=',v)
#     def f2():
#         v =300      #L
#         print('f2.v=',v)
#     f2()
# f1()
# print('全局的v=',v)

l = [1, 2]
def f1():
    l = [3, 4, 5]
f1()
print(l) #因为f1()只制造两个局部变量

# def f2():
#     l =l + [3,4,5]
# f2()
# print(l)    #出错 一个作用域内的一个变量不能是局部又是全局

def f3():
    l[:] = [3,4,5]
f3()
print(l)    #[3,4,5]

