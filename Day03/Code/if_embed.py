# 此示例用if　语句嵌套来实现下面程序的功能

#２．输入一年中的月份1-12, 输出这个月在哪几个季度。
   # 如果输入的是其他的数，则提示您输错了

m = int(input("请输入１－１２的月份："))
if 1 <= m <= 12:
    print("用户输入是合法的月份")
    if m <= 3:
        print(m,"月在第一季度")
    elif m <= 6:
        print(m,"月在第二季度")
    elif m <= 9:
        print(m,"月在第三季度")
    else:
        print(m,"月在第四季度")
else:
    print("您输入错误")






# m = int(input("请输入１－１２的月份："))
# if 1 <= m <=3:
#     print(m,"月在第一季度")
# elif 4 <= m <= 6:
#     print(m,"月在第二季度")
# elif 7 <= m <= 9:
#     print(m,"月在第三季度")
# elif 10 <= m <= 12:
#     print(m,"月在第四季度")
# else:
#     print("您输错了")