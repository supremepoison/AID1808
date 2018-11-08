# 已知有列表:
#                     L = [2, 3, 5, 7]
#                     1) 写一个生成器函数，让此函数能够动态提供数据，数据为原列表的数字的平方加1
#                     2) 写一个生成器表达式，让此表达式能够动态提供数据，数据为原列表的数字的平方加1
#                     3） 生成一个列表，此列表内的数据是原列表数据的平方加1

L = [2, 3, 5, 7, 10, 15]
# 1.
# def gen(L):
#     for i in L:
#         yield i**2 + 1

# it = iter(gen(L))
# for i in range(len(L)):

#     print(next(it))
# 2.
# gen = (i ** 2 +1 for i in L)
# it = iter(gen)
# for i in range(len(L)):

#     print(next(it))
# 3.
gen = [i ** 2 +1 for i in L]
print(gen)

    





