

# def power2(x):
#     return x ** 2

# #生成一个可迭代对象,此可迭代对象可以生成1-9的自然数的平方

# for x in map(power2,range(1,10)):
#         print(x)

#生成一个可迭代对象,可迭代对象可以生成
#   1**4 2**3 3**2 4**1
#pow(x,y,z=None)

# for x in map(pow, range(1,5),
#                     range(4,0,-1)):
#     print(x)

for x in map(pow, [1,2,3,4],
                    [4,3,2,1],
                    range(5,10)):
    print(x)