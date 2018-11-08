#此示例示意try-except 语句的基本语法和用法

def div_apple(n):
    print ("现在有%d个苹果,您想分给几个人:"%n)
    s = input("请输入人数:")
    count  = int(s)     #可能触发ValueError错误
    result = n /count   #ZeroDivisionError
    print("每个人分了%d个苹果"% result)
try:
    div_apple(6)
# except ValueError as err:
#     print("分苹果时发生值错误异常,已捕获并转为正常状态")
#     print("发生错误的原因是:",err)
# except ZeroDivisionError:
#     print("没有人来拿苹果,苹果被收回")
except(ValueError, ZeroDivisionError):
    print("苹果拿回")
    
    
print("程序正常结束")