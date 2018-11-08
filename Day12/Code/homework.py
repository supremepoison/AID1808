# 练习:
#   1. 写程序算出1~20 的阶乘的和
#     1! + 2! + 3! + 4! + .... + 20!


# def mysum(n):
#     if n == 1:
#         return 1
#     return n * mysum(n-1)
# a = sum(map(mysum,range(1,21)))
# print(a)


#  2. 已知有列表:
#         L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#     1) 写一个函数 print_list(lst) 打印出所有的数字
#         print_list(L)  # 3 5 8 10 13 ....
#     2) 写一个函数 sum_list(lst) 返回列表中所有数字的和
#         print(sum_list(L))  # 106
#     注:
#        type(x) 函数可以返一个对象的类型
#        如:
#           >>> type(20) is int  # True
#           >>> type([3, 5, 8]) is list  # True
#           >>> type(20) is list  # False
L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
# def print_list(lst):
#     for i in lst:
#         if type(i) is list:
#             print_list(i)
#         else:
#              print(i, end = ' ')
            
    
    
# # print_list(L)

# def sum_list(lst):
#     s  = 0
#     for i in lst:
#         if type(i) is list:   #如果是列表 则s+= 列表所有元素的和
            
#             s +=sum_list(i)
#         else:   #如果i是整数
#             s +=i
#     return s
# print(sum_list(L))

# 3. 改写之前的学生信息的程序,要求添加四个功能:
#       | 5)  按学生成绩高-低显示学生信息 |
#       | 6)  按学生成绩低-高显示学生信息 |
#       | 7)  按学生年龄高-低显示学生信息 |
#       | 8)  按学生年龄低-高显示学生信息 |





list = []#用于保存学生信息的列表
def input_student():
    
    while True:
        n = input("Enter your name('Enter' == quit):")
        if not n:
            break
        d ={}
        a = input("Enter your age:")
        s = input("Enter your score:")

        d['name'] = n
        d['age'] = a
        d['score'] = s
        for i in list:
            if n == i['name']:
                print("This name already exists")
                main()
            
        list.append(d)
    return list

    
def print_student(list):
    width = 0
    for y in list:
        

        biggest=len(max(y['name'],y['age'],y['score'] ))
        if biggest > width:
            width = biggest

        
    print('+'+ '-'*(width+15) + '+' + '-'*(width+15) +'+'+ '-'*(width+15) +'+')

    print('|'+'name'.center(width+15)+ '|'+ 'age'.center(width+15)+ '|'+ 'score'.center(width+15)+ '|')

    print('+'+ '-'*(width+15) + '+' + '-'*(width+15) +'+'+ '-'*(width+15) +'+')

    for d in list:
        line = '|'+d['name'].center(width+15)+ '|'+ d['age'].center(width+15)+ '|'+ d['score'].center(width+15)+ '|'
        print(line)
    print('+'+ '-'*(width+15) + '+' + '-'*(width+15) +'+'+ '-'*(width+15) +'+')

def delete_student():
    n = input("Enter the name:")
    for i in list:
        if i['name'] == n:
            list.remove(i)
            print("delete successfully")
            return list
    else:
            print("nobody")
            
def modify_student():
    n = input("Enter the name :")
    for i in list:
        if i['name'] == n:
            score = input("Enter the new score:")
            i['score'] = score
            print("modify successfully")
            return list
            
    else:
            print("nobody")





# def max_min_score():
#     def get_score(x):
#         return x['score']  
#     L = sorted(list, key = get_score, reverse = True)
#     print_student(L)
#     return L

def max_min_score():
    L = sorted(list, key = lambda d:d['score'], reverse = True)
    print_student(L)
    return L

def min_max_score():
    L = sorted(list, key = lambda d:d['score'])
    print_student(L)
    return L

 
 
def max_min_age():
    L = sorted(list, key = lambda d:d['age'], reverse = True)
    print_student(L)
    return L

def min_max_age():
    L = sorted(list, key = lambda d:d['age'])
    print_student(L)
    return L
    

def show_menu():
    print('+-------------------------------------+')
    print('| 1) 添加学生信息                        |')
    print('| 2) 显示学生信息                        |')
    print('| 3) 删除学生信息                        |')
    print('| 4) 修改学生信息                        |')
    print('| 5) 按学生成绩高-低显示学生信息         |')
    print('| 6) 按学生成绩低-高显示学生信息         |')
    print('| 7) 按学生年龄低-高显示学生信息         |')
    print('| 8) 按学生年龄低-高显示学生信息         |')       
    print('| q) 退出                                |')
    print('+-------------------------------------+')




def main():
    global list
    while True:
        #打印菜单
        #show_menu()
        show_menu()

        s = input('请选择:')
        if s == '1':
            list = input_student()
             
        elif s == '2':
            print_student(list)

        elif s == '3':
            delete_student()

        elif s =='4':
            modify_student()

        elif s == '5':
            max_min_score()
             
        elif s == '6':
            min_max_score()

        elif s == '7':
            max_min_age()

        elif s =='8':
            min_max_age()    
        
        elif s == "q":
            break
print(main())
             


   
