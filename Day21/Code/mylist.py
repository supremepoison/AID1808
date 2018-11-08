class MyList:
    
    def __init__(self, iterable = ()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return '%s' % self.data
    def __neg__(self):
        # L = [-x for x in self.data]
        # L = (-x for x in self.data)
        L = map(lambda x : -x, self.data)
        return MyList(L)

    def __pos__(self):
        L = map(lambda x : abs(x), self.data)
        return MyList(L)


L = MyList([1, -2, 3, -4, 5])
L2 = -L
print(L2)
L3 = +L
print(L3)