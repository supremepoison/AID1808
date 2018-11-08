# 练习:
#         查看 
#         >>>Help(print)
#         猜想print() 函数是形参列表如何定义的?
def myprint(*args, sep=' ', end = '\n' ):
    print(*args, sep=sep, end=end)



print()
myprint(1,2,3,4)
myprint(1,2,3,4, sep = '#')
myprint(1,2,3,4, sep = '#', end ='\n')
myprint('===========================')

