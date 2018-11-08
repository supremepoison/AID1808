# 此示例示意nonlocal的用法

# var = 100
# def f1():
#     var = 200
#     print('f1.var=',var)
#     def f2():
#         var = 300
#         print('f2.var=',var)
        
#     f2()
#     print("f1.var=",var)
# f1()
# print("全局的var=",var)

var = 100
def f1():
    var = 200
    print('f1.var=',var)

    def f2():
        var = 300
        print('f2.var=',var)

        def f3():
            nonlocal var  
            var = 400
            print('f3.var=',var)

        f3()
        print('f2.var=',var)
    f2()
    print("f1.var=",var)
f1()
print("全局的var=",var)