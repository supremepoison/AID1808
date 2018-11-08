

class MyList:
    '''
    创建一个自定义列表类,此MyList内部用列表来存储信息
    '''

    def __init__(self, iterable=()):
        self.data = [x for x in iterable]
    def __repr__(self):
        return 'MyList(%s)' % self.data
    def __len__(self):
        '''
        此方法必须返回整数
        '''
        # return len(self.data)
        return self.data.__len__()
    def __reversed__(self):
        return self.data[::-1]

    def __abs__(self):
        lst = [abs(x) for x in self.data]
        L = MyList(lst)
        return L



myl = MyList([1, -2, 3, -4])
print(myl)
print('myl 的长度是:', len(myl))
print(abs(myl))
print(reversed(myl))

myl2 = MyList()
print(myl2)