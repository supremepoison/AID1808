        
'''这是我的一个自定义模块

这是一个模块的文档描述部分
此模块有两个函数和两条数据
'''

# 此示例示意自定义模块  mymod 及导入方法
def mysum(n):
    print("正在计算1+2+3+...+", n, '的和')


def myfac(n):
    print("正在计算%d" % n)


name1 = "audi"
name2 = "tesla"
if __name__ == '__main__':

    print("在mymod.py模块内的__name__属性值为:")
    print(__name__)

    print("Hello my noble guest")
