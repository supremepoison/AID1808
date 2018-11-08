# 写一个函数 get_age() 用来获取一个人的年龄信息
#         此函数规定用户只能输入1~140之间的整数，如果用户输入其它的数则直接触发ValueError类型的错误


def get_age():
    a = int(input("Enter your age:"))
    if 1<= a <= 140:
        return a
    else:
        raise ValueError




try:
    age = get_age()
    print("用户输入的年龄是,",age)
except ValueError as err:
    print("用户输入的不是1-140的数字,获取年龄失败")