#此示例示意try-except 语句的基本语法和用法

def div_apple(n):
    print ("现在有%d个苹果,您想分给几个人:"%n)
    s = input("请输入人数:")
    count  = int(s)     #可能触发ValueError错误
    result = n /count   #ZeroDivisionError
    print("每个人分了%d个苹果"% result)
try:
    div_apple(6)
    print("分苹果结束")

except:
    print("有异常发生")
else: 
    print("没有异常发生")
finally:
    print("我是try里的finally语句")
    print("我一定会被执行")
    
    
print("程序正常结束")