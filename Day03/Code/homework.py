#1.北京出租车计价器

# k = int(input("输入公里数："))
# m = 13
# if k <= 3:
#     print("金额为：", m)
# if k > 3:
#     if k <= 15:
#         m = m + (k-3)* 2.3
#         print("金额为：", round(m))
#     elif k > 15:
#         m = m + (k - 3)* 2.3 + (k - 15)* 1.15
#         print("金额为：", round(m))
    
#*********************************************
#2.输入一个学生的三科成绩:
#{1}
a = int(input("请输入语文成绩："))
b = int(input("请输入数学成绩："))
c = int(input("请输入英语成绩："))
# d = max(a, b ,c)
# e = min(a, b ,c)
# g = (a+b+c)/3

# print("max:",d)
# print("min:",e)
# print("average:",g)




#{2}
# if a >= b:
#     a, b = b, a
# if c >= a:
#     c, b = b, c
# if  a >= c:
#     a, c= c, a
# d = (a+b+c)/3
# print(b, "max", a, "min")
# print("average:",d)

#{3}
# if a > b:
#     if a > c:
#         biggest = a
#     else:
#         biggest = c 
# else:
#     if b > c:
#         biggest = b
#     else:
#         biggest = c     
# print(biggest)

#{4}
# biggest = a
# if b > biggest:
#     biggest = b
# if c > biggest:
#     biggest = c
# print(biggest)  

#*********************************************
#3.给处一个年份，判断是否为闰年并打印结果

# year = int(input("输入年份："))

# if year%4 == 0 and year%100 != 0 or year%400 == 0:

#     print(year, "闰年")
# else:
#     print(year, "不是闰年")

#*********************************************
#4.　BMI(Body Mass Index)指数，又称身体质量指数
w = float(input("输入体重："))
h = float(input("输入升高："))
bmi = w/h**2

if bmi < 18.5:
    print(bmi, "体重过轻")
elif 18.5 <= bmi < 24:
    print(bmi, "正常范围")
else:
    print(bmi, "体重过重")   





        
    
# for i in range(100, 1000):
#     a = i // 100
#     b = (i % 100)//10
#     c = i % 10
#     if i == a ** 3+b ** 3+c ** 3:
#         print(i)




# 判断一个５位数，是否回文数
# 例如：输入１２３４５，不是
# 如数１２３２１　是的

# i = int(input("输入五位数"))

# a = i//10000
# b = i//1000%10
# c = i//100%10
# d = i%100//10
# e = i % 10

# if a == e and b == d:
#     print(i)
# else:
#     print("error")


