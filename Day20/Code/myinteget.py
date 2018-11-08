

class MyInteger:
    def __init__(self, value):
        self.data = int(value)

    def __int__(self):
        '''
        此方法必须返回整数
        '''
        return self.data

    def __float__(self):
        return float(self.data)

a1 = MyInteger('100')
i = int(a1)     #将InTeger类型转为整数
print(i)

i1 = float(a1)
print(i1)

c = complex(a1)
print(c)

d = bool(a1)
print(d)