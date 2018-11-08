# 练习:
# #             1.写一个lambda表达式
# #                 fx  = lambda n :
# #                 此表达式创建的函数判断n这个数的2次方+1能否被5整除,如果能返回True,否则返回False

# fx = lambda n : (n**2+1) % 5 == 0
# print(fx(3))
# print(fx(4))



# 2.写一个lambda表达式来创建函数,此函数返回两个形参变量的最大值
#                 def mymax(x,y):

#                 mymax = lambda...
#                 print(mymax(100,200))
#                 print(mymax("ABC", "123"))

# def mymax(x,y):
#     return max(x,y)

# mymax = lambda x,y: max(x,y)
mymax = lambda x,y: x if x>y else y

print(mymax(100,200))
print(mymax("ABC", "123"))
