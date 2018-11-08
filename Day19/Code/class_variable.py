


#此示例示意类变脸的定义方法和用法
class Car:
    #类变量,用于保存车对象的个数
    total_count = 0     #创建类变量


print(Car.total_count)          #读取类变量的值 
Car.total_count += 100          #修改类变量
print(Car.total_count)          #100


c1 = Car()
print(c1.total_count)           #借助对象访问类变量
c1.total_count = 999            #创建实例变量
print(c1.total_count)           #999
print(Car.total_count)          #100


#类变量可以通过此类的对象的__class__ 属性间接访问

c1.__class__.total_count = 50000
print(c1.total_count)           
print(Car.total_count)          

