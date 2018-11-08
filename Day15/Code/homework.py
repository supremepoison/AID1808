# 作业:
#      1. 一个球从100米高空落下，每次落地后反弹高度是原高度的一半，再落下
#       1)写程序算出皮球在第10次落地后反弹高度是多高?
#       2)打印出共经过了多少米的路程

#     2. 分解质因数: 输入一个正整数，分解质因数:
#     如输入:
#       90
#     则打印:
#       '90=2*3*3*5'
#       (质因数是指小数最小能被原数整除的素数(不包含1))


# def bounce(n):
#     height = 100
#     distance = 100
#     for i in range(n):
#         if 1 == 0:
#             distane = distance +  height /2
#             height = height /2
#         else:
#             distance += height
#             height = height /2

#         if i == 9:
       
#             print("The distance between top and bottom:",height)
#     print(distance)
# a = int(input("Enter"))
# bounce(a)


# def prime(n):
#     L = []
#     print(n, '=', end= ' ')
#     for i in range(1,n):
#         if n % i ==0 and i != 1:
#             L.append(i)
#             n = n // i
#             if n % i == 0:
#                 L.append(i)
#                 n = n // i
#                 if n <= i and n != 1 :
#                     L.append(n)
#     for i in range(len(L)):
#         if i == (len(L) - 1):
#            print(L[i])
#         else:   
#             print(L[i], '*', end = ' ')
#     # return L
# a = int(input("Enter a numer:"))
# prime(a)
    
        