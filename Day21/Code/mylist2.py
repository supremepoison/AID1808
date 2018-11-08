#此示例示意 in/not in 运算符重载方法


class MyList:
    
    def __init__(self, iterable = ()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return '%s' % self.data
    
    def __contains__(self, e):
        return e in self.data

    


L = MyList([1, -2, 3, -4, 5])
print(3 in L)
print(3 not in L)
print(4 in L)
print(4 not in L)