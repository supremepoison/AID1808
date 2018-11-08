

#此示例示意将自定义的类定义为可迭代对象

class MyList:
    
    def __init__(self, iterable = ()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return '%s' % self.data

    def __iter__(self):
        '''
        要求必须返回迭代器
        '''
        return MyList_Iterator(self.data)

class MyList_Iterator:
    '''
    此类用来创建能访问MyList类型的迭代器
    '''
    def __init__(self, data):
        self.data = data    #先绑定可迭代对象的数据
        self.current_index = 0 #设置迭代器的起始位置为 0 

    def __next__(self):
        '''
        此方法用来实现迭代器协议
        '''
        if self.current_index >= len(self.data):
            raise StopIteration
        #拿到当前索引指向的数
        r = self.data[self.current_index]
        #将索引数指向下一个数
        self.current_index += 1
        return r    #f返回当前的数 

L = MyList('ABCD')
print(L)
for x in L:
    print(x)

# it= iter(L)
# while True:
#     print(next(it))