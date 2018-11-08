class MyList:
    
    def __init__(self, iterable = ()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return '%s' % self.data
    
    def __add__(self, rhs):
        return self.data + rhs.data
    def __mul__(self, rhs):
        return self.data * rhs

    


L1 = MyList(range(1,4))
L2 = MyList([4,5,6])
L3 = L1 + L2
print(L3) #Mylist([1,2,3,4,5,6])
L5 = L1 * 3
print(L5)   #Mylist([1,2,3,1,2,3,1,2,3])