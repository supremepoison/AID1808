# 练习:
#             创建一个字典:
#                 d = {'name' : 'tarena'. 'age': 15}
#                 为此字典添加地址(address)键,对应的值为"北京市海淀区"

#创建字典
#d = {'name' : 'tarena', 'age': 15}                 #字面值

#d = dict(name ='tarena',age=15)                    #关键字传参

# d = dict(
#     (['name', 'tarena'], ('age',15))              #可迭代对象创建字典
# )

# d = {}                                            #先创建一个空字典,
# d['name'] = 'tarena'                              #在往里边添加
# d['age'] = 15


d ['address'] = '北京市海淀区'
print(d)