class Human:
    def set_info(self,name,age,address = '不详'):
        ''' 此方法用来给人对象添加 "姓名" , "年龄" 和"家庭住址" '''
        self.name = name
        self.age = age
        self.address =address

    def show_info(self):
        '''显示此人的信息'''
        print(self.name,self.age,'岁,','家庭住址:',self.address)


s1 = Human()
s1.set_info('小张', 20, '深圳市南山区')

s2 = Human()
s2.set_info('小李', 18)

s1.show_info()
s2.show_info()

s3 = Human()
s3.set_info('小狗',90)
s3.show_info()
s3.set_info('小狗',90,'圪僚沟')
s3.show_info()