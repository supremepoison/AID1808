

class Mynumber:
    '''
    此类用于定义一个自定义的数字类型
    '''
    def __init__(self, value):
        self.data = value       #data数据

    def __str__(self):
        '''
        重写object类中的__str__(obj)
        '''
        print('Mynumber.__str__被调用')
        return "数字%d" %self.data 

n1 = Mynumber(100)
s1 = str(n1)
s2 = repr(n1)
print(s1)
print(s2)