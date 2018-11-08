# 练习：
#     1.写程序 输入一个三角形的宽和高 打印相应的三角形
#         如：
#             输入3
#             1） 
#             *
#             **
#             ***
#             2） 
#               *
#              ** 
#             ***
#             3)
#             ***
#             **
#             *
#             4)
#             ***
#              **
#               *
#     2. 写程序，任意输入一个整数，判断这个数是否为素数(prime)
#         素数（也叫质数），只能被1和自身整除的正整数
#             如：2 3 5 7 11 13 17...
#         提示：
#             用排除法 ： 当判断x是否为素数时，只要让x分别除2,3,4,5，...x-1，
#              只要有任何一个数能， 则说明x不是素数，否认为x素数

#     3.
#         编写程序求下列多项式的值：
#             Sn = 1/1 -1/3 + 1/5 - 1/7+ ....
#             1)求1000000个这样的分数相加的值是多少？
#             2）将上一步的值乘以4打印出来，是多少？
#     4.算出 100-999之间的水仙花数    

#***********************************************************************
# #1.1
# a = int(input("Enter a numebr :"))
# for i in range(1, a+1):
#     print("*" * i)
      

# 1.2
# a = int(input("Enter a numebr :"))
  
# for i in range(1, a+1):
#     print((a-i) * " " + "*"* i)
    

# #1.3
# a = int(input("Enter a numebr :"))
# for i in range(a, 0, -1):
#     print("*" * i)
   
# 1.4
# a = int(input("Enter a numebr :"))
  
# for i in range(a, 0, -1):
#     print((a-i) * " " + "*"* i)
    
#*******************************************************************
# #2.
# a = int(input("Enter a numnber :"))
# if a < 2:
#     print("not primes")
# else:

#     for i in range(2,a):
        
#         if a % i == 0:
#             print("不是")
#             break
        
#     else:
#         print("是")
   
# # # 3.
# sn = 0.0
# a = 1
# for i in range(1, 1000000, 2):
    
#     if a % 2 ==1:
#         sn += 1/i
#     else:
#         sn -= 1/i 
#     a +=1
# print(sn)   
# print(sn*4)
# #**********************************************
# sn = 0.0
# fenmu = 1
# i = 0
# b = 1
# while i < 100000:
#     r = b *1/fenmu
#     sn += r

#     b *=-1
#     fenmu +=2
#     i+=1
# print(sn)

#4
# for i in range(100, 1000):
#     a = i // 100
#     b = (i % 100) //10
#     c = i %10
#     if i == a ** 3+ b**3+ c**3:
#         print(i)

#列表
# for i in range(100, 1000):
#     s = str(i)
#     a = int(s[0])
#     b = int(s[1])
#     c = int(s[2])
#     if i == a ** 3+ b**3+ c**3:
#         print(i)
#循环嵌套
for a in range(1,10):
    for b in range(10):
        for c in range(10):
            if a*100+b*10+c  == a ** 3+ b**3+ c**3:
                print(a,b,c)




       
     