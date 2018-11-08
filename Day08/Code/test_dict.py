#   1.将如下数据形成一个字典 seasons:
#             键          值
#             1       '春季有 1,2,3 月'
#             2       '春季有 4,5,6 月'
#             3       '春季有 7,8,9 月'
#             4       '春季有 10,11,12 月'
#         2.让用户输入一个整数,代表季度,打印这个季度的信息,如果用户输入的信息不存在与字典内,则打印"信息不存在"

1.

seasons = {}
seasons[1] = '春季有 1,2,3 月'
seasons[2] = '夏季有 4,5,6 月'
seasons[3] = '秋季有 7,8,9 月'
seasons[4] = '冬季有 10,11,12  月'






a = int(input("Enter a numer :"))
if a not in seasons:
    print("信息不存在")
else:
    print(seasons[a])