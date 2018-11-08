# 练习：
#     1.输入一个字符串，把输入的字符串中的空格全部去掉（包括字符串中间的空格）
#         打印原字符串及长度
#         打印处理后的字符串及长度
#     2.写程序， 输入三行文字，让这三行文字在一个方框内居中显示
#         如：
#             请输入： hello!
#             请输入： I'm a man.
#             请输入： I hate you.
#         打印如下：
#             +-------------+
#             |    hello!   |
#             |  I'm a man  |
#             | I hate you. |
#             +-------------+
#**********************************************************
#1.
# a = str(input("Enter: "))
# b = a.replace(" ", '')
# print("original：",a, "length:", len(a))
# print("new:",b, "wdith:", len(b))
#***********************************************************

#2.
a = str(input("Enter 1:"))
b = str(input("Enter 2:"))
c = str(input("Enter 3:"))


length = max(len(a), len(b), len(c))

top = "+" + "-"*length + "+"

print(top)

center1 = a.center(length)
left1 = "|" + center1 + "|" 
print(left1)

center2 = b.center(length)
left2 = "|" + center2 + "|" 
print(left2)

center3 = c.center(length)
left3 = "|" + center3 + "|" 
print(left3)
 
print(top)



