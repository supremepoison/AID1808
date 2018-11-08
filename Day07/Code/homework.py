# 1. 有一些数存于列表中:
#     L= [1,3,2,1,6,4,2,....98,82]
#         1)将列表L中出现的数字存入到另一个列表L2中
#         要求:
#             重复出现多次的数字只在L2中保留一份(去重)
#         2)将列表中出现两次的数字存在于列表L3中,在L3中只保留一份
#     2.计算出100以内的全部素数,将这些素数存于列表中,然后打印出列表中的这些素数
#     3.生成前40个斐波那契数列中的数:第三项为前两项之和 n >=2
#        1 1 2 3 5 8 13......
#        要求将这些数保存与列表中,打印这些数


# # 1.
# L= [1,3,2,1,6,4,2,1,1,1,1,1,1,1,2,2,2,2,3,3,3,4,1,5,6,5,5,7,7,7,8,8,8,9,9,9]
# L2 = []
# L3 = []
# for i in L:
#     if i not in L2:
#         L2.append(i)
#     if L.count(i) == 2 and i not in L3:
#         L3.append(i)
        
# print(L2)
# print(L3)

# 2.  

# l = []
# for x in range (2,101):
#     t = []
    
#     for y in range(1,x+1):
#         if x % y == 0:
#             t.append(x)
#     if len(t)>2:
#         continue
#     else:
#         l.append(x)
# print(l)


# #如果这个数是素数加入到列表中
# l = []
# for x in range(1,101):
#     #r如果x是素数,则把x加入到l中,否则跳过
#     isprime = True #先假设x是素数
#     #如果x不是素数,就把isprime置为False
#     if x < 2:
#         isprime = False
#     else:
#         for i in range (2,x):
#             if x  % i == 0: #整除就不是素数
#                 isprime = False
#                 break
#     if isprime:         #一定为素数
#         l.append(x)
# print(l)
# # 3. 
# l = [1,1]
# for i in range(0,38):
#     a = l[i]
#     b = l[i+1]
#     c = a +b
#     l.append(c)

# print(l)

l = []
a = 0   #代表当前一个数的前一个数

b = 1   #代表当前斐波那契数
while len(l)<400000:
    l.append(b)
    c = a+b #求出下一个斐波那契数
    a = b
    b = c

print(l)

    
    

           
    
    
        
