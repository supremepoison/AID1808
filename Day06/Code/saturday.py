#输出40个斐波那契数:第三项为前两项之和 n >=2
# 1 1 2 3 5 8 13......
# a = 1
# b = 1
# l = []
# for i in range(1, 100):
#     c =  a + b
#     if len(l)<40:
#         print(a, end = " ")
#         l.append(a)
#     else:
#         break
#     if len(l)<40:
#         print(b, end = " ")
#         l.append(b)
#     else:
#         break
#     if len(l)<40:
#         print(c, end = " ")
#         l.append(c)
#     else:
#         break
#         
#     a = c + b
#     b = c + a 
        
# print()
#*******************************************************************************
# #输出一个字符串
#     打印出这个字符串出现过的每个字符和它出现过的次数
# a =  input("Enter something: ")
# n = 1
# l = list(a)
# print(l)
# for i in a:
#     if i == l:
#         print(i)

# #1.
# for i in range(1,10):
    
#     for j in range(1, i+1):
#         print(j, end = " ")
#     print()
#***********************************
# #2.
# a = 0
# for i in range(1,11):
#     a +=99
# print(a)
#***************************
#3
# a = 0
# for i in range(1, 101):
#     a +=i
# print(a)
#**************
#4
# a = 1
# for i in range(1,11):
#     a *= i
# print(a)
#****************************************
# 5.
# a = 2
# for i in range(1,21):
#     if i < 20:
#         a= a*2
# print(a)
#***************************************
# 6.
# a = 0
# for i in range(1,1000):
#     if i % 2 ==1:
#         a +=i
# print(a)
# 7.
# a = 0
# for i in range(1,1000):
#     if i % 3 ==0 or i % 17 ==0:
#         a +=i
# print(a)
# 8. 
# a = 0
# for i in range(1,1000):
#     if i % 3 ==0 and i % 5 ==0 and i % 7 ==0 :
#         a +=i
# print(a)
# 9.
# a = 0
# for i in range(1,100):
#     if i % 3 ==0 or i % 7 ==0 and i % 3 ==1 or i % 7 == 1:
#         a +=1
# print(a)
# 10
# a = 0
# for i in range(1,100):
#     if i % 7 ==0 and i % 2 ==1:
#         a +=1
# print(a)
# 11

# l = []
# for i in range(1,100):
#     l.append(i)
#     b = [i]
    
#     c = [i+1]
#     print(b,"+",c )

# n = 1
# for i in range(2,101):
#     print(n, '+', i, '=', n+i)
#     n +=1
#12
#a = int(input("Enter a numnber :"))
# for i in range(2,a):
    
#     if a % i == 0:
#         print("不是")
    
# else:
#     print("是")
# 13
# a = input("Nnter a number:")
# l = list(a)
# b = len(l)
# d = 0 
# for i in range(b):
#     c = l[i]
#     d += int(c) 
# print(d)
# 14
# a =0 
# for i in range(10000, 100000):
#     if str(i) == str(i)[::-1]:
#         print(i)
#         a += 1
        
# print(a)
# 15
# a = input("Enter a numer :")
# l = len(a)
# if l < 11:
#     b = a[::-1]
#     print(int(b))
# 16
# for i in range(100,1000):
#     a = i//100
#     b = i //10 %10
#     c = i %10
#     if i == a**3+ b**3+ c**3:
# #         print(i)
# 17
# a = int(input("n = "))
# b = 100
# c = 0
# for i in range(a):
#     if i < 2:
#         c +=100
#     else:
#         b =b/2
#         c +=b
# print(c) 
# 18
# a = input("Enter a number :")
# b = 0
# d = 0
# for i in range(1,6):
#     b = a * i
#     c = int(b)
#     d = d +c
#     print(c)
# print(d)
# 19
# for a in range (10):
#     for b in range(10):
#         for c in range(10):
#             d = str(a)+str(b)+str(c)
#             e = str(c)+str(b)+str(a)
#             f = int(d)
#             g = int(e)
#             if f + g == 1333:
#                 print(f)
# 20
# import random
# l =[]
# for i in range(30):
#     a = random.randint(48,123)
#     b = chr(a)
#     if b.isalpha() or b.isdigit():
#         l.append(b)
#         if len(l) == 6:
#             print(l)
        
                    
# print()
# 21
# a = input("Enter a sentence: ")
# c= 1
# for i in a:
#     if i == " ":
#         c +=1
# print(c)
# 22
# a = input("Enter a sentence: ")
# c = 0
# for i in a:
#     if i.isdigit():
#         c +=int(i)
# print(c)
# 23
# a = input("Enter a sentence: ")
# l = []
# c = 0
# for i in a:
#     b =a.count(i)
#     if i not in l:
#         l.append(i)
#         print(l[c],b)
#         c+=1
# 24
# a = int(input("Enter a number: "))
# for i in range(3,a):
#     if a % i == 0:
#         print("no")
#         break
# else:
# #     print("yes")
# 25
# a = int(input("Enter a numer: "))
# for i in range(1,a+1):
#     for j in range(1,a+1):
#         print(i,'*', j,end = ' ')
#         if i == j:
#             break
#     print()


     





                
            
                 


    

    
    




    

    

    





     

       
   
        

    




