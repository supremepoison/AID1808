# 1.写一个生成器函数,给出开始值begin,和终止值end,此生成器函数生成begin-end 范文内全部素数,不包括end
#                     如:
#                     def prime(begin, end):
#                         ....

#                     L = list(prime(10,20))


def prime(begin ,end):
    for i in range(begin ,end):
        prime = True
        if begin < 2:
            prime = False
        else:
            for j in range(2, i):
                if i % j  ==0:
                    prime = False

        if prime:
            yield i

L = list(prime(2,20))
print(L)

        