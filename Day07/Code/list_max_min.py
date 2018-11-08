# 练习:(list_max_min.py)
#         1.输入三个数,存于列表中,打印出这三个数的最大值,最小值和平均值
#         2.写程序,让用户循环输入一些整数,当输入 -1时,结束输入,将这些整数存于列表中
#             1)打印您共输入了几个有效的数
#             2)打印您输入的数的最大值是多少?
#             3)打印您输入的数的平均值是多少?
L = []
for i  in range(1,4):
    a = int(input("Enter %d numbers:" % i))
    L.append(a)
print(L)
average = sum(L)/3
print(max(L),min(L),average)


# L = []
# while True:
#         a = int(input("Enter some numbers: "))
#         if a == -1:
#             break
#         else:
#             L.append(a)
# print(L)
# print("有效数字的个数:",len(L))
# print("Max:", max(L))
# print("Average:", sum(L)/len(L))







