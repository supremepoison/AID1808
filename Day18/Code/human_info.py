# 两个人:
#         1.姓名: 张三, 年龄:35
#         1.姓名: 李四, 年龄:8
#     行为:
#         1. 教别人学东西　teach
#         2. 工作赚钱 work
#         3. 借钱 borrow 
#         4. 显示自己的信息 show_info
#     事情:
#         张三　教　李四 学 python
#         李四　教　张三　学 王者荣耀
#         张三　上班赚了 1000　元钱
#         李四　向 张三　借了 200 元钱
#         35　岁的　张三　有钱 800元，它学会的技能: 王者荣耀
#         8 岁的 李四 有钱 200元， 它学会的技能: python

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 0
              

    def teach(self, other, skill):

        # print(self.name, 'teach', other.name, skill)

        other.skill = skill

    

    def work(self, money):
        self.money = money

    def borrow(self, name, money):
        if name.money > money:
            self.money = money
            name.money -= money
        else:
            print('failed')
       
    def show_info(self):
        print(self.age, self.name, self.money, self.skill)



zhang = Human('zhang', 35)
li = Human('li', 8)

zhang.teach(li, 'python')
li.teach(zhang, 'LoL')

# zhang.work(1000)
li.borrow(zhang, 200)

zhang.show_info()
li.show_info()
