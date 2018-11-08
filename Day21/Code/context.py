
#此示例示意自定义用 with 管理的对象



class A:
    '''
    此类的对象将可用于with语句中
    '''
    def __enter__(self):
        print('已经进入到了with语句的内部')
        return self     #把自己返回由 as 来绑定
    
    def __exit__(self, exc_t, exc_v, exc_tb):
        '''
        exc_t 用来绑定异常类型
        exc_v 用来绑定异常对象
        exc_tb 用来绑定追踪对象
        在没有异常时,三个形参都绑定None
        '''
        if exc_t is None:
            print('正常退出with语句')
        else:
            print('异常退出')
with A() as a:
    print('这是with语句内部的print')
    int(input('请输入整数:'))
