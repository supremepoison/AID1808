# 输入一段字符串，打印出这个字符串中出现过的字符及出现过的次数：
#             如：
#             输入: ABCDABCABA
#         打印：
#             a:4次
#             b:3次
#             c:2次
#             d:1次
# #方法一 字典
# a = input("Enter something:")
# b = {}
# for i in a :
#     if i not in b:
#         b[i] = 1
#     else:
#         b[i] +=1
# for i in b:
#     print(i,':',b[i],'次')

#方法二
# a = input("Enter something:")
# #先将字符串去重,放入到列表l 中
# l = []          #用来存放出现过的字符
# for i in a :
#     #如果i没有在l中,说明第一次出现
#     if i not in l:
#             l.append(i)

# for i in l:
#     print(i,':',a.count(i),'次')