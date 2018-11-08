class Mynumber :
    def __init__(self, value):
        self.data = value
    def __repr__(self):
        return '%d' % self.data

    def __add__(self, rhs):
        
        return self.data + rhs.data
    def __sub__(self, rhs):
        
        return self.data - rhs.data
n1 = Mynumber(100)
n2 = Mynumber(200)

n3 = n1 + n2
n4 = n1-n2

print(n3)
print(n4)
