

# 此示例示意用super显示的调用被覆盖的方法

class A:
    def work(self):
        print("A.work被调用")

class B(A):
    def work(self):
        '''
        此方法会覆盖父类的work方法
        '''
        print("B.work被调用")
    
    def mywork(self):
        #调用自己(B类)的方法
        self.work()
        
        super(B,self).work()

        super().work()
        #调用父类(A类)的方法

b = B()
b.work()
# A.work(b)
# super(B,b).work()
b.mywork()
