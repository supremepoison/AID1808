

#此示例示意初始化方法的定义及自动调用

class Car: 
    def __init__(self, c, b, m):
            self.color = c
            self.brand = b
            self.model = m
    def run (self, speed):
        print(self.color, self.brand, self.model, '正在以', speed, 'km/hour 的速度行驶')

a4 = Car('silver','audi','A4')
a4.run(199)

m3 = Car('grey', 'BMW', 'm3')
m3.run(200)