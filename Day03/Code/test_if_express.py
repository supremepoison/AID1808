#写程序，输入一个数，用条件表达式计算这个数的绝对值并打印出来

num = int(input("数字："))
num = -num if num < 0 else num
print(num) 