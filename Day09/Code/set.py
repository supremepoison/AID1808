# 练习:
#         经理有: 曹操,刘备,孙权
#         技术员有: 曹操,孙权,张飞,关羽
#         用集合求:
#             1.是经理也是技术员的人有谁?
#             2.是经理,但不是技术员的人有谁?
#             3.是技术员,但不是经理的人有谁?
#             4.张飞是经理吗?
#             5.身兼一职的人有谁?
#             6.经理和技术员共有几个人?

# manager = {'曹操','刘备','孙权'}
# tech = {'曹操','孙权','张飞','关羽'}

# a = manager & tech
# b = manager - tech
# c = tech - manager
# d = '张飞' in manager
# e = manager ^ tech
# f = len(manager|tech) 

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

a = (1,2,3,4)
b =set(a)

print(b)
b[2] = 3

print(b)