#  1.写一个函数 myadd2, 实现给出两个数,返回这两个数的和
#                 如:
#                     def myadd2(x,y):
#                     ...
#                     a = int(input("Enter the first number :"))
#                     b = int(input("Enter the first number :"))
#                     print("The sum of two number is :",myadd(a,b))


# def myadd2(x,y):
    
#     return x+y
# a = int(input("Enter the first number :"))
# b = int(input("Enter the second number :"))
# print("The sum of two numbers is :",myadd2(a,b))

#  2.写一个函数mymax,返回三个数中最大的一个值
#                     def mymax(a,b,c):
#                     ...
#                     print(mymax(100,200,300))

# def mymax(a,b,c):
#     # return max(a,b,c)

#     # z = a if a > b else b
#     # z = z if z > c else c
#     # return z


    
# print(mymax(100,200,300))
# print(mymax('AB','200','ab'))


#  3.写一个函数 input_numbers
#                 def input_numbers():
#                 ...
#                 此函数用来获取用户循环输入的正整数,当用户输入负数时结束输入
#                 将用户输入的数字以列表的形式返回
#                 再用内建函数max min sum 求用户输入数的最大最小值 和

def input_numbers():
    l = []
    while True:
        num = int(input("Enter some numbers:"))
        if num <0:
            return l
        if num ==0:
            pass
        else:
            l.append(num)
    
L = input_numbers()
print(L)
print("Max:",max(L))
print("Minx:",min(L))
print("Sum:",sum(L))
