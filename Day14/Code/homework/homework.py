# 作业:
#   1. 模拟斗地主发牌，牌共 54张
#     黑桃('\u2660'), 梅花('\u2663'), 红桃('\u2665'), 方块('\u2666')
#     A2-10JQK
#     大王,小王
#     三个人，每个人发17张，底牌留三张
#     要求:
#       输入回车,打印第1个人的17张牌
#       输入回车,打印第2个人的17张牌
#       输入回车,打印第3个人的17张牌
#       输入回车,打印三张底牌

#   2. 将学生信息管理程序拆分为模块
#     要求:
#       1. 主事件循环放在main.py中
#       2. show_menu 函数放在menu.py中
#       3. 写学生操作相关的函数放在 student_info.py中
#     主模块为 main.py

# 1. 
# import random

# number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
# color = ['\u2660','\u2663','\u2665','\u2666']
# card_list = [j+i for i in number for j in color ]
# card_list.append("Joker")
# card_list.append("joker")

# # print(card())
# a = input("回车发牌")
# p1 = random.sample(card_list,17)
# if not a:
#     print(p1)

# for i in p1:
#     card_list.remove(i)
# # print(card_list)

# a = input("回车发牌")
# p2 = random.sample(card_list,17)
# if not a:
#     print(p2)
# for i in p2:
#     card_list.remove(i)

# a = input("回车发牌")
# p3 = random.sample(card_list,17)
# if not a:
#     print(p3)
# for i in p3:
#     card_list.remove(i)

# a = input("回车发牌")

# if not a:
#     print("底牌")
#     print(card_list)


import random
poke = ['Joker', 'joker']
kinds = ['\u2660','\u2663','\u2665','\u2666']

numbers = ['A'] + [str(x) for x in range(2,11)] + list('JQK')

for k in kinds:
    for n in numbers:
        poke.append(k + n )

poke2 = poke.copy()

random.shuffle(poke2)
p1 = poke2[0:17]
p2 = poke2[17:34]
p3 = poke2[34:51]
bottom = poke2[51:]
input("输入回车键发牌")
print(p1)
input("输入回车键发牌")
print(p2)
input("输入回车键发牌")
print(p3)
input("输入回车键看底牌")
print(bottom)


