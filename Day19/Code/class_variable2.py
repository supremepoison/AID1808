#此示例示意类变脸的定义方法和用法
class Car:
    #类变量,用于保存车对象的个数
    total_count = 0     #创建类变量
    def __init__(self, info):
        self.info = info
        print('汽车', info, '被创建')
        self.__class__.total_count += 1
    def __del__(self):
        print('汽车', self.info, '被干了')
        self.__class__.total_count -= 1
        

c1 = Car('BYD E6')
c2 = Car('Jili E7')

print('当前有%d个汽车对象' % Car.total_count)

del c1
print('当前有%d个汽车对象' % Car.total_count)
