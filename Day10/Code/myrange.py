#  练习:(myrange.py)
#         写一个 myrange函数,参数可以传入1-3个,实际含义与range函数相同
#         此函数返回符合range(...)函数的列表
#         如:
#             L = myrange(4)
#             print(L) #[0,1,2,3]
#             L = myrange(4,6)
#             print(L) #[4,5]
#             L = myrange(1,10,3)
#             print(L) #[1,4,7]
#             注:可以调用range

# def myrange(start, stop=None, step =1):
#     l =[]
#     if stop is None:
#         for i in range(start):
#             l.append(i)
#     else:
#         for i in range(start,stop,step):
#             l.append(i)

#     return l
# L = myrange(10,1,-1)
# print(L)

def myrange(a, b=None, c=None):
    if b is None:
        start = 0
        stop = a
    else:
        start = a
        stop = b
    if c is None:
        step =1
    else:
        step = c
    return list(range(start,stop,step))
L = myrange(10,1,-1)
print(L)