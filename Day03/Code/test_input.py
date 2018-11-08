#ａ.输入两个整数，分别用变量　x,y 来绑定
  #  　１．计算两个数的和，　并打印结果
   # 　２．计算两个数的积，　并打印结果
   # 　３．计算　x的y次方并打印结果

x = input("x:")
y = input("y:")
x = int(x)
y = int(y)
print("两个数的和", x + y)
print("两个数的积", x * y)
print("x 的　y　次方：", x ** y)


# b.分三次输入当前的小时，分钟，秒数
  #      在终端打印出距离　０．０．０　过了多少秒？

sec = int(input("sec:"))
min = int(input("min:"))
hour = int(input("hour:"))
print(hour,":", min,":", sec, "距离0:0:0过了:", hour * 3600 + min * 60 + sec, "秒")