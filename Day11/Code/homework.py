# # 练习:
# # #     1. 看懂下面的程序在作甚
# #         def fx(f, x ,y):
# #             print(f(x,y))
# #         fx((lambda a,b: a+b), 100, 200)
# #         fx((lambda a,b :a**b),3,4)






#     # 2.给出一个整数n,写一个函数来计算
#     #     1+2+3+4+...+n  的值并返回结果
#     #     要求用函数来做
#     #     如:
#     #     def mysum(n):
#     #     ...    
#     #     print(mysum(100))
#     #     print(mysum(10))
#     # ************************************
# # def mysum(n):
# #     score = 0
# #     for i in range(1,n+1):
# #         score +=i
# #     return score
# #     return sum(range(1,n+1))
# # print(mysum(100))
# # print(mysum(10))
# #***************************************       





# # 3.给出一个整数n,写一个函数来计算n!(n的阶乘)
# #     n!= 1*2*3*4...*n
# #     def myfac(n):
# #         ....
# #     print(myfac(5))     #120

# # def myfac(n):
# #     score = 1
# #     for i in range(1,n+1):
# #         score *=i
# #     return score
# # print(myfac(5))

# #**************************************    
#     # 4.给出一个整数n,写一个函数来计算
# # #     #     1+2**2+3**3+...n**n
# # def multi(n):
# #     score = 0
# #     for i in range(1,n+1):
# #         score += i**i
# #     return score
# # print(multi(2))

# def f(n):
#     return sum(map(lambda x : x**x, range(1,n+1)))
# print(f(2))


# def a(n):
#     def b(x):
#         return x += n**n
#     return b
# c = a(2)
# print(c(2))
# # #************************************
#     # 5.写程序打印杨辉三角(6层)
#     #      1
#     #     1 1
#     #    1 2 1
#     #   1 3 3 1
#     #  1 4 6 4 1  
# #     # 1 5 10 10 5 1

# # def triangle(n):
# #     list = [[1]]
# #     for i in range(2,n+1):
# #         list.append([1]*i)
# #         print
# #         for j in range(1,i-1):
# #             #  list[4][1] =list[3][1]+list[3][0]
# #             #  list[4][2] =list[3][2]+list[3][1]
# #              list[i-1][j] =list[i-2][j]+list[i-2][j-1]
           
# #     for a in range(n):
# #         print(' '*(n-a), end =' ')
# #         for b in range(a+1):
            
# #             c= list[a][b]
# #             print('%2d' % c, end =' ')
# #             if a == b:
# #                 print()

#第一步,制造相应的列表
def get_next_list(L):
    #用给定一行L,返回下一行
    #如:L为[1,2,1]则返回[1,3,3,1]
    rl= [1] #最左边的1
    #算中间的数字(循环获取从0开始的索引)
    for i in range(len(L)-1):
        v = L[i]+ L[i+1]
        rl.append(v)

    rl.append(1)#最右边的1
    return rl
    #第二步,生成全部的行放到一个整体的列表L中,并返回
def yh_list(n): #ｎ为行数
    #　如果n 为3, 最终返回的列表是：
    #    [1],[1,1],[1,2,1]
    rl = []
    L = [1]
    while len(rl) < n:
        rl.append(L)  #加入当前行
        L = get_next_list(L)    #计算出下一行准备加入

    return rl
#第三步，把杨辉三角的列表转为字符串列表
def get_yh_string(L):
    rl = []
    for line in L:
        #line = [1,2,1]
        str_lst = [str(x) for x in line]
        #str_lst = ['1','2','1']
        s = ' '.join(str_lst) #s = '1 2 1'
        rl.append(s)

    return rl
#打印杨辉三角
def print_yh_triangle(L):
    max_len = len(L[-1])
    for s in L:
        print(s.center(max_len))

L = yh_list(6)
SL =get_yh_string(L)
print_yh_triangle(SL)















#     # 6.实现带界面的学生信息管理系统的项目:
#     # +-------------------------------------+
#     # | 1) 添加学生信息                       |
#     # | 2) 显示学生信息                       |
#     # | 3) 删除学生信息                       |
#     # | 4) 修改学生信息                       |
#     # | q) 退出                              |
#     # +-------------------------------------+
#     # (要求用函数来实现,每个功能写一个函数写值相对应)

# list = []#用于保存学生信息的列表
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
#         for i in list:
#             if n == i['name']:
#                 print("This name already exists")
#                 main()
            
#         list.append(d)
#     return list

    
# def print_student():
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

# def delete_student():
#     n = input("Enter the name:")
#     for i in list:
#         if i['name'] == n:
#             list.remove(i)
#             print("delete successfully")
#     else:
#             print("nobody")
#     return list
            
# def modify_student():
#     n = input("Enter the name :")
#     for i in list:
#         if i['name'] == n:
#             score = input("Enter the new score:")
#             i['score'] = score
#             print("modify successfully")
#     else:
#             print("nobody")
#     return list
            
# def main():
#     global list
#     while True:
#         #打印菜单
#         #show_menu()
#         print('+-------------------------------------+')
#         print('| 1) 添加学生信息                       |')
#         print('| 2) 显示学生信息                       |')
#         print('| 3) 删除学生信息                       |')
#         print('| 4) 修改学生信息                       |')
#         print('| q) 退出                              |')
#         print('+-------------------------------------+')

#         s = input('请选择:')
#         if s == '1':
#             list = input_student()
             
#         elif s == '2':
#             print_student()

#         elif s == '3':
#             delete_student()

#         elif s =='4':
#             modify_student()
        
#         elif s == "q":
#             break
# print(main())