#  写一个生成器函数 myeven(start, stop) 用来生成从 start 开始到stop 结束区间内的一些列偶数(不包含stop)
#                 如:
#                     def myeven(start, stop):
#                         ...
#                     evens = list(myeven(10,20))
#                     print(evens) [10,12,14,16,18]
#                     for x in myeven(5,10):
#                         print(x) #6 8 
#                     L = [x for x in myeven(0,10)]
#                     print(L)

def myeven(start, stop):
    # while start<stop:
    #     if start % 2 == 0:
    #         yield start
    #         start +=2
    #     else:
    #         start += 1
    #         yield start
    #         start +=2
    for x in range(start, stop):
        if x % 2 == 0:
            yield x
        




evens = list(myeven(10,20))
print(evens) 
for x in myeven(5,10):
    print(x) 
L = [x for x in myeven(0,10)]
print(L)
