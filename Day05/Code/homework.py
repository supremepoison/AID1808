#  1.打印从零开始的浮点数，每个数增加0.5，打印出10 以内这样的数
#         2.写程序：
#             1/1 + 1/3 + 1/5 + 1/7 + ... +1/99 的和
#         3.输入一个整数表示三角形的宽度和高度，打印出如下的三角形：
#          如：
#             请输入三角形的宽度 ： 4
#             打印如下：
#             *
#             **
#             ***
#             ****
#         4.写程序：
#             输入一个整数代表正方形的宽和高，打印如下的正方形：
#                 如:
#                     请输入宽度：5
#                 打印正方形如下：
#                 1 2 3 4 5
#                 2 3 4 5 6
#                 3 4 5 6 7
#                 4 5 6 7 8
#                 5 6 7 8 9
#*************************************************************
# #1.
# i = 0.0
# while i <10:
#     print(i)
#     i +=0.5
# #*************************************************************
# 2. 

# i = 1
# s = 0
# while i < 100:
#     s += 1/i
#     i +=2
# print(s)
#*************************************************************
# 3.
# a = int(input("Enter length:"))
# i = 1
# while i <= a:
#     print("*"* i)
#
# 4.
a = int(input("Enter length:"))
i = 0
while i <a :
    b = 1
    while b <=a:
        print("%02d" % (i+b), end =" ")
        b +=1
    print()
    i +=1



        