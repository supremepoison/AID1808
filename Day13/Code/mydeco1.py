

#此示例用装饰器改变原来函数的调用流程(业务流程)
#银行业务

#此装饰器用来增加权限验证功能
def privile_check(fx):
    def fn(x,y):
        print("验证中")
        fx(x,y)
    return fn

#此装饰器用来增加短信提醒功能
def message_send(fn):
    def fy(x,y):
        fn(x,y)
        print("正在发送短信给",x,'...')
    return fy

@message_send
@privile_check
def save_money(name,x):
    print(name, '存钱', x, '元')
@privile_check
@message_send
def withdraw(name, x):
    print(name,'取钱',x, '元')


save_money("小王", 200)
save_money("小赵", 400)
withdraw('小李', 500)

