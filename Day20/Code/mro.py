

# 此示例示意__mro__类属性和用法


class A:
    def go(self):
        print('A')

class B(A):
    def go(self):
        print('B')
        super().go()        #C

class C(A):
    def go(self):
        print('C')

class D(B, C):
    def go(self):
        print('D')
        super().go()        #B

d = D()
d.go()
print(D.__mro__)

b = B()
b.go()
print(B.__mro__)

