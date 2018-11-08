

#此示例示意多继承的语法

class Car:
    def run(self,speed):
        print('汽车以', speed, 'km/h的速度行驶')

class Plane:
    def fly(self,height):
        print('飞机以海拔', height, '米高度飞行')

class PlaneCar(Car, Plane):
    '''
        PlaceCar 同时继承自汽车类和飞机类
    '''
    pass

p = PlaneCar()
p.run(100)
p.fly(200)
