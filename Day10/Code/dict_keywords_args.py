# 此示例示意双星号字典形参的定义和调用

# def fun(**kwargs):
#     print("关键字传参个数是", len(kwargs))
#     print('kwargs= ', kwargs)

# fun(a=1, b='bbbb', c =[2,3,4])      #关键字传参
# fun()
def fn(*args, **kwargs):
    print('args=', args)
    print('kwargs=', kwargs)
fn(1,2,*'abc', *{'sadfds'}, (1,2.3),b=3, **{'a': 'vsdfdf'})