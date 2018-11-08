# # # 此示例示意命名关键字形参的定义的方式和调用方法

# # def f1(*,c ,d):     #*之后的形参为命名关键字形参
# #     print('c=', c)
# #     print('d=', d)

# # #f1(3,4)             #wrong
# # f1(d=4, c=3)        #correct

# # d1 = {'c':30,'d':40}
# # f1(**d1)




# def f2(a,b, *args, c, d):
#     print(a,b)
#     print(args)
#     print(c,d)

# f2(1,2,3,4, d=200 , c=100)

