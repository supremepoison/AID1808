# 此示例示意函数名绑定函数,函数名是变量


def fn():
    print("hello world")
    return 1

# f1 = fn
# print(f1)       #<function fn at 0x7f3e8a019f28>

# fn()
# f1()
f2 =fn()

print(f2)


# def f1():
#     print("hello f1")

# def f2():
#     print("hello f2")

# f1, f2 = f2, f1
# f1()
           