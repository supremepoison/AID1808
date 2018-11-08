#此示例示意 索引和切片 运算符重载方法


class MyList:
    
    def __init__(self, iterable = ()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return '%s' % self.data

    def __getitem__(self, i):

        if type(i) is int:
            print('索引')

        elif type(i) is slice:
            print('切片')
            print('起始值',i.start)
            print('结束值',i.stop)
            print('步长值',i.step)


        return self.data[i]
    
    def __setitem__(self, i, v):
        self.data[i] = v
       
    
    def __delitem__(self, i):
        del self.data[i]

    


L = MyList([1, -2, 3, -4, 5])
print(L[3:1:-1])
print(L[0])
L[1] = 2
print(L)
del L[1]
print(L)