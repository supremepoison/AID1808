
# 此示例示意复合赋值运算符的重载

class MyList:
    
    def __init__(self, iterable = ()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return '%s' % self.data
    
    def __add__(self, rhs):
        return self.data + rhs.data
    def __mul__(self, rhs):
        return self.data * rhs

    def __iadd__(self, rhs):
        self.data.extend(rhs.data)
        return self

    


L1 = MyList(range(1,4))
print(id(L1))
L2 = MyList([4,5,6])
L1 += L2
print(id(L1))
print(L1)

