# 作业:
#         1.写一个函数叫isprime(x) 判断x是否是素数 如果是素数,返回True,否则返回False
#         2.写一个函数prime_m2n(m, n) 返回从m开始,到n结束的范围内的素数 不包括(n), 返回这些素数的列表,并打印
#             如:
#                 L= prime_m2n(5, 10)
#                 print(L) #[5,7]
#         3.写一个函数primes(n), 返回指定范围n以内的素数,不包含n ,的全部素数的列表,并打印这些素数
#         1) 打印 100 以内的全部素数
#         2) 打印200 以内的全部素数的和
#         4.改写之前的学生信息管理程序:
#             改为用两个函数实现
#             1)写函数input_student()来获取学生信息,
#             当输入姓名为空时结束输入,形成字典组成的列表并返回
#             2)写函数print_student(L) 将上述函数得到的打印成表格显示


# 1.
# def isprime(x):
#     if x ==2:
#         return True
#     for i in range(2,x):
#         if x % i == 0:
#             return False
#         else:
#             return True
# print(isprime(7))


# 2. 
# def prime_m2n(m,n):
#     l = []
#     for i in range(m,n):
#         isprime = True
#         if i < 2:
#             isprime = False
#         else:
#             for x in range(2,i):
#                 if i % x ==0:
#                     isprime  = False
#         if isprime:
#             l.append(i)
#     return l
# print(prime_m2n(2,10))
# 3.
# def primes(n):
#     l = []
#     for i in range(n):
#         isprime = True
#         if i <2:
#             isprime = False 
#         else:
#             for x in range(2,i):
#                 if i % x == 0:
#                     isprime = False
#         if isprime:
#             l.append(i)
#     return l  
# print(primes(100))
# print(sum(primes(100)))

# 4. 
# list = []
# def input_student():
#     while True:
#         n = input("Enter your name:")
#         if not n:
#             break
#         d ={}
#         a = input("Enter your age:")
#         s = input("Enter your score")

#         d['name'] = n
#         d['age'] = a
#         d['score'] = s
#         list.append(d)

#     return list
# input_student()

# def print_student(list):
#     width = 0
#     for y in list:
        

#         biggest=len(max(y['name'],y['age'],y['score'] ))
#         if biggest > width:
#             width = biggest

        
#     print('+'+ '-'*(width+15) + '+' + '-'*(width+15) +'+'+ '-'*(width+15) +'+')

#     print('|'+'name'.center(width+15)+ '|'+ 'age'.center(width+15)+ '|'+ 'score'.center(width+15)+ '|')

#     print('+'+ '-'*(width+15) + '+' + '-'*(width+15) +'+'+ '-'*(width+15) +'+')

#     for d in list:
#         line = '|'+d['name'].center(width+15)+ '|'+ d['age'].center(width+15)+ '|'+ d['score'].center(width+15)+ '|'
#         print(line)
#     print('+'+ '-'*(width+15) + '+' + '-'*(width+15) +'+'+ '-'*(width+15) +'+')
#     print_student(list)


