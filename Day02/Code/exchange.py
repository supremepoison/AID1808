#变量交换练习：
  #  已知有两个变量
  #      a 绑定 10000
   #     b　绑定　20000
   # 问，　在不创建新对象的情况下，如何让a 和b 交换绑定的对象

# a=10000
# b=20000

# print("交换前",a,b)
# #第一种
# temp=a
# a=b
# b=temp
# print("交换后",a,b)

# #第二种
# a ,b = b, a #序列赋值


# a =1 
# b =2
# print(a ,b)
# c = a
# a = b
# b = c
# print(a , b)

a = 1
b = 2
print(a, b)

a, b = b ,a
print( a, b)
