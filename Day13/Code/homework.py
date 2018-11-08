# 作业:
#     1.编写函数 fun , 其功能是机选下列多项式的和
#         f(n) = 1+ 1/1!+ 1/2!+....+1/n!
#         当n=20时,求和
#     2. 写一个程序，打印电子时间:
#       格式为:
#         HH:MM:SS
#       每过一秒钟刷新一次
#     3. 编写一个闹钟程序，启动时设置定时时间, 到时间后打印一句:
#       "时间到",然后程序退出


# # 1.
# import math
# # def fun(n):
# #     s = 1 
# #     for i in range(1,n+1):
# #         s += 1/math.factorial(i)
# #     print(s)
# # fun(20)

# def f(n):
#     s = sum(map(lambda x :1/math.factorial(x), range(n+1)))
#     return s
# print(f(20))
# # 2. 
# import time



# while True:
#     t = time.localtime()

# #     print('%02d:%02d:%02d' % (t[3:6]),end = '\r')
#     time.sleep(1)

3. 
import time
a = int(input("Enter the hour:"))
b = int(input("Enter the minute:"))
c = int(input("Enter the seconds:"))


while True:
    t = time.localtime()
    print('%02d:%02d:%02d' % (t[3:6]),end = '\r')
    
    
    time.sleep(1)
    if (a, b, c) == t[3:6]:
        print("Times out")
        break


# def alarm(h,m):
#     print("Time:%02d: %02d" % (h,m))
#     while True:
#             #得到当前时间
#         t = time.localtime()
#         t = t[3:5]
#         if t ==(h, m):
#             print("Times out")
#             break




# alarm(a,b)



    







