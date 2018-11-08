# 此示例示意 写一个函数, 此函数的功能是给它两个数,让它把最大值的数据打印出来

def my_max(a,b):
    m = a
    if b >m:
        m = b
    print("最大值的数据为:",m)

a = int(input("a="))
b = int(input("b="))

my_max(a,b)
