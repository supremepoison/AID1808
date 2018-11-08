

#用列表推到式生成 1-100 内所有奇数的平方的列表


#L = [x**2 for x in range(1,100,2)]
#print(L)



# 写程序. 输入一个开始的整数值用begin绑定
#             输入一个结束的整数用end绑定
#                 将从begin开始到end结束的所有偶数存于列表中,并打印(建议用列表推到式)


# begin = int(input("Begin:"))
# end = int(input("End:"))

# L = [x for x in range(begin,end) if x % 2 == 0]
# print(L)


# 2. 写程序,让用户输入很多个整数(包含正整数和负整数)保有存在于列表L中,输入0时结束输入.然后把列表L中的所有整数存于L1中,把列表L中所有负数存于列表L2中
#         打印原列表L和整数列表L1和负数列表L2
# L =[]
# while True:
#     a = int(input("Enter some numbers:"))
#     if a ==0:
#         break
#     L.append(a)
#     L1 = [i for i in L if i >0]
#     L2 = [i for i in L if i <0]
# print(L)
# print(L1)
# print(L2)





# #
# #         用字符串"ABC" 和 "123" 生成如下列表:
# #             ['A1','A2','A3','B1','B2','B3','C1','C2','C3']

# L = [a+b for a in 'ABC'
#         for b in ['1','2','3']]
# print(L)



# 1.已知有一个字符串:
#         s = '100,200,300,500,800'
#         将其转化为数字组成的列表,列表内部为整数:
#             L = [100,200,300,500,800]
#  2.用列表推到式生成如下列表:
#         L = [1, 4, 7, 10, ... 100]
#  3.用列表推到式生成如下列表(思考题)
#         [[1,2,3], [4,5,6],[7,8,9]]

# # 1. 
# s = '100,200,300,500,800'
# L = s.split(",")
# a = [int(a) for a in L]
# print(a)
# 2.
# L = [x for x in range(1,101,3)]
# print(L)
# 3. 
# # L = [[int(a),int(b),int(c)] for a in '147' 
# #             for b in '258' if int(a)== int(b)-1
# #             for c in '369' if int(b) == int(c)-1]
# *****************************************************
# L = [[x, x+1, x+2] for x in range(1,8,3)]
# ***************************************************
# L = [[y for y in range(x, x+3)]
#         for x in range(1, 8, 3)]
# ****************************************************
# L = []
#  for x in range(1, 8, 3):
#      temp = []
#      for y in range(x, x+3):
#          temp.append(y)
#     L.append(temp)


# print(L)
