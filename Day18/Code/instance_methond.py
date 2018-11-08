
#此示例示意为Dog类添加吃, 睡, 玩, 等实例方法.以实现Dog对象的相应行为



class Dog:
    '''这是一种可爱的小动物'''
    def eat(self,food):
        '''此方法用来描述小狗吃的行为
        '''
        print('The id %d of ' % id(self), end = '')
        print('the dog is eating:', food)

    def sleep(self,hour):
        print('The id %d of the dog has slept %d hours' % (id(self), hour))

    def play(self,something):
        print('The id %d of the dog is playing %s' %(id(self),something))
       # return 方法内可以用return返回对象的引用






dog1 = Dog()
dog1.eat('shit')
dog1.sleep(7)
dog1.play('ball')

dog2 = Dog()
dog2.eat('dog1')
dog2.sleep(17)
dog2.play('dog1')

Dog.play(dog2,'cat') 