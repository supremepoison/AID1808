# 作业:
#   1. 打印 9 x 9 乘法表:
#     1x1=1
#     1x2=2 2x2=4
#     1x3=3 2x3=6 3x3=9
#     ......
#     1x9=9 ..............   9x9=81

# def multiplay():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print(j, '*', i, '=', i*j, end = ' ')
#             if i == j:
#                 print()

# multiplay()



#   2. 写一个生成器函数 myxrange(start, stop, step) 来生成一系列整数
#      要求功能与range完全相同
#      不允许调用range函数和列表
#     然后用自己写的myxrange函数求 1 ~ 100内奇数的平方和

# def myrange(start, stop = None, step = 1):
#     i = 0
#     if stop == None:
#         while i < start:
#             yield i 
#             i += step
#     if step > 0:
#         while start < stop:
#             yield start 
#             start += step
#     elif step < 0:
#         while stop < start:
#             yield start
#             start += step
    
# for i in myrange(5, 10, 1):
#     print(i)

# # s = 0
# for i in myrange(1,100,2):
#     s += i**2
# print(s)
    
# def myxrange(start, stop =None, step = 1):
#     if stop is None:
#         stop = start
#         start = 0
    
#     if step > 0:
#         while start < stop:
#             yield start
#             start += step
#     elif step < 0:
#         while start > stop:
#             yield start
#             start += step

# L = [x for x in range(1,10,1)]
# print(L)
        


#   3. 写一个myfilter生成器函数,功能与filter函数功能完全相同
#      如:
#         def myfilter(fn, iter1):
#              ...
#         L = [x for x in myfilter(
#             lambda x: x%2, range(10)
#         )]  # L = [1, 3, 5, 7, 9]

# def myfilter(fn, iter1):
#     for i in iter1:
#         if fn(i) ==  True:
#             yield i
 
# L = [x for x in myfilter(
#             lambda x: x%2, range(10)
#         )]
# print(L)




#   4. 将以前所有练习自己不看之前的代码重写一遍    