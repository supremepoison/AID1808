# 练习：
#         写一个程序，打印一个高度为4行的矩形方框
#         如：
#             请输入矩形宽度：10
#         打印：  
#             ##########
#             #        #
#             #        #
#             ##########
# # 方法一
a = int(input("请输入矩形宽度："))
b = "#" *a
c = "#"
d = " " * (a-2)

# print(b)
# print(c, d, c, sep = '')
# print(c, d, c, sep = '')
# print(b)

# 方法二
print(b)
print(c + d + c)
print(c + d + c)
print(b)