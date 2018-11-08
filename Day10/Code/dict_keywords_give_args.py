# 此示例示意字典关键字传参


def myfun1(a,b,c):
    print("the value of a:",a)
    print("the value of b:",b)
    print("the value of c:",c)

d1 = {'c':33, 'b':22, 'a':11}

myfun1(**d1)


