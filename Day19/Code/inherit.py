

class Human:
    '''
    此类用于描述人类的共性
    '''
    def say(self, what):
        print('说:', what)
    
    def walk(self, distance):
        print('走了', distance, '公里')
    def star(self):
        print('***********************')

h1 =Human()
h1.say('天蓝蓝')
h1.walk(5)
h1.star()


class Student(Human):
    def study(self,course):
        print('不想学:',course)
s1 = Student()
s1.say('累的一批')
s1.walk(23)
s1.study('python')
s1.star()

class Teacher(Student):
    def teach(self, lesson):
        print('我们一起:',lesson)

t1 =Teacher()
t1.teach('爬楼梯')
t1.say('go die')
t1.study('抽皮条')
t1.walk(4)