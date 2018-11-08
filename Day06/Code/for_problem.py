#  1.for 语句的 range 调用顺序：
#      示意：
#      请问此程序打印的结果是什么？
#       i = 6
#       for x in range(1,i):                    #range 函数只调用一次
#       print("x= ", x, "i= ", i)           #此 print 函数 会执行 5次
#       i -= 1
        


# i = 6
# for x in range(1,i):
#     print("x= ", x, "i= ", i)
#     i -= 1
#*****************************************************************************
# 2. for 语句变量列表里的变量可能不被创建
            
#             for x in range(4, 0):
#                 print(x)
#             esle:
#                 print("循环结束后x的值是"， x)          #报错


# for x in range(4, 0):
#     print(x)
# else:
#     print("循环结束后x的值是", x) 
#**********************************************************************
# 3.for语句中用break语句中断执行时，else子句不会执行
#             示例见：   
#                 for x in range(10):
#                     print(x)
#                     if x == 3:
#                         break
#                 else:
#                     print("for语句结束")
for x in range(10):
    print(x)
    if x == 3:
        break
else:
    print("for语句结束")

