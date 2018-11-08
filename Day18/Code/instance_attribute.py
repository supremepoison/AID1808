

#此示例示意创建和使用实例属性
class Dog:
    '''这是一种可爱的小动物'''
    def eat(self,food):
        '''此方法用来描述小狗吃的行为
        '''
        print(self.color, self.kinds, '正在吃', food)

        #以下让当前的小狗自己记住吃的是什么
        self.last_food = food

    def show_info(self):

        print(self.color, self.kinds, '上次吃的是', self.last_food)


dog1 = Dog()
dog1.kinds = '哈士奇'           #创建属性
dog1.color = 'black and white'  #创建 属性 color
dog1.color = 'white'            #修改属性color
print(dog1.color, dog1.kinds)
dog1.eat('shit')
dog1.show_info()

dog2 = Dog()
dog2.kinds = '藏獒'
dog2.color = 'grey'
dog2.eat('food')