# 此示例示意raise无参用法

def fa():
    print("fa开始")
    raise ValueError("故意制造的一个错误!")
    print("fa结束")

def fb():
    print("fb开始")
    try:
        fa()
    except ValueError as err:
        print("fa里发生了已处理")
        #此处如果要将err再次向上传递
        raise 
    print("fb结束")
try:
    fb()
except ValueError:
    print("再一次收到fb内部发生的错误!")