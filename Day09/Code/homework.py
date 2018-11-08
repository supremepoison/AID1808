# 作业:
#         1.写一个get_chinese_char_count(s) 函数.
#         此函数实现的功能是给定一个字符串,返回这个字符串中中文字符的个数
#         def get_chinese_char_count(s):
#         ...

#         s= input("请输入中引文混合的字符怕:")
#         print("您输入中文字符的个数是:",get_chinese_char_count(s))

#         2.定义两个函数:
#             sum3(a,b,c) 用于返回三个数的和
#             pow3(x)     用于返回x的三次方(立方)
#         用以上函数计算:
#             1) 计算1 的立方+2的立方+3的立方
#             2) 计算 1+2+3的立方和的立方
# 1. 
# def get_chinese_char_count(s):
#     num = 0
#     for i in s:
#         if ord(i) > 127:
#             num +=1
#     return num


# s= input("请输入中引文混合的字符怕:")
# print("您输入中文字符的个数是:",get_chinese_char_count(s))
2. 
def sum3(a,b,c):
    return a+b+c
def pow3(x):
    return x**3
a = pow3(1)+pow3(2)+pow3(3)
b = pow3(sum3(1,2,3))
print("计算1 的立方+2的立方+3的立方",a)
print("计算 1+2+3的立方和的立方",b)
    