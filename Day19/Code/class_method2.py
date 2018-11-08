

#此示例示意类方法的定义及调用

class A:
    v = 0

    @classmethod
    def get_v(cls):
        return cls.v

    @classmethod    
    def set_v(cls,value):
        cls.v = value       #设置类变量v=value



a = A()
print(a.get_v())
a.set_v(100)
print(a.get_v())
print(a.v)








