# # 作业:
# #     1.已知有两个等长的列表
# #         list 1 = [1001,1002,1003,1004]
# #         list 2 = ['Tom','Jerry','Rose','Jack']
# #         生成如下字典
# #         {'To吗:1001, 'Jerry':1002, 'Rose':1003, 'Jack':1004}

# #     2.任意输入多个学生的姓名,年龄,成绩,每个学生信息存入一个字典中,然后再放入列表中(每个学生信息需要手动输入)
# #         如:
# #             请输入姓名: tarena
# #             请输入年龄: 15
# #             请输入成绩: 99
# #             请输入姓名: name2
# #             请输入姓名: <直接回车结束输入>
# #         在程序内部生成如下列表:
# #             l = [{'name': tarena, 'age':15, 'score':99}, {'name': name2,....}]

# #         1)打印出上述列表
# #         2)以下列表格的形式打印出上述信息
# #         +------------+------------+------------+
# #         |   name     |    age     | score      |
# #         +------------+------------+------------+

# # # # 1.
# # list1 = [1001,1002,1003,1004]
# # list2 = ['Tom','Jerry','Rose','Jack']
# # d = {list2[i]:list1[i] for i in range(4)}
# # print(d)

# # 2.


# width = len('+------------+')
# l = []
# while True:
#     n = input("Enter your name:")
#     if not n:
#         break
#     d ={}
#     a = input("Enter your age:")
#     s = input("Enter your score")
    
#     d['name'] = n
#     d['age'] = a
#     d['score'] = s
#     l.append(d)

# print(l)

# print("+------------+------------+------------+")
# print("|   name     |    age     |    score   |")
# print("+------------+------------+------------+")
# # for i in range(len(l)):
# #     n1 = l[i]['name']
# #     a1 = l[i]['age']
# #     s1 = l[i]['score']

# #     data = '|'+ n1.center(width-2)+ '|'+ a1.center(width-2)+ '|'+ s1.center(width-2)+ '|'
# #     print(data)

# for d in l:
#     line = '|'+d['name'].center(width-2)+ '|'+ d['age'].center(width-2)+ '|'+ d['score'].center(width-2)+ '|'
#     print(line)
# print("+------------+------------+------------+")





