#此示例示意return语句的作用和用法


def say_hello():
        print("print aaa")
        print("print bbb")
        #return              #等同于 return None
        #return 1+2
        return[1,2,3]
        print("print ccc")

r = say_hello()
print(r)

print("ENd")