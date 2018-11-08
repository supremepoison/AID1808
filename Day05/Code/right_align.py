# 练习：
#     输入三行文字，让这三行文字一次以20个字符的宽度右对齐输出
#     如：
#         请输入第一行：hello
#         请输入第二行：hi
#         请输入第三行：yo
#     输出结果：
#                 hello
#                    hi
#                    yo
#     做完上面的题后再思考：
#         能否以最长字符串的长度进行右对齐显示（左侧填充空格）


a = input("Enter first line:")
b = input("Enter second line:")
c = input("Enter third line:")

# d = "%20s" % a
# e = "%20s" % b
# f = "%20s" % c

g = max(len(a), len(b), len(c))
# d = " "*(g-len(a)) + "%s" % a
# e = " "*(g-len(b)) + "%s" % b
# f = " "*(g-len(c)) + "%s" % c

# print(d)
# print(e)
# print(f)


fmt = "%" + str(g) + "s"
print(fmt % a)
print(fmt % b)
print(fmt % c)