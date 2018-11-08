# 1.写一个函数,mysum 可以传入任意个实参的数字,返回实参的和

# def mysum(*args):
#     s= 0
#     for i in args:
#         s +=i
    
#     return s

# print(mysum())
# print(mysum(1,2,3,-2.0))

# 2.写一个函数min_max() 
#                 此函数至少要传一个参数,并返回全部这些数的最小值,最大值,(形成元祖,最小在前,最大在后)
#                 调用此函数,得到最小值和最大值并打印出来

def min_max(a, *args):
   
    return min(a,*args),max(a,*args)
print(min_max(1,2,3))
x, y = min_max(2,3,4,4,5,6,6757,3,78,6)
print("Min:",x)
print("Max:",y)
#print(min_max())  #报错

# def min_max(a, *args):
#     zuixiao = a
#     for x in args:
#         if x < zuixiao:
#             zuixiao = x

#     zuida = a
#     for i in args:
#             if i > zuida:
#                 zuida = i
#     return zuixiao, zuida
# print(min_max(1))
# x, y = min_max(2,3,4,4,5,6,6757,3,78,6)
# print("Min:",x)
# print("Max:",y)