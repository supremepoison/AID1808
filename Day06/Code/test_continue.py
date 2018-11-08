# 练习：
#             1.输入一个整数，代表开始用 begin绑定
#               输入一个整数，代表结束用end 绑定
#               打印 begin——end （不包含end） 之间的全部奇数

#             2. 求1-100 之间所有不能被2， 3， 5， 7整除的数，
#                a.打印出这些数
#                b.并计算和 


# begin = int(input("Begin: "))
# end = int(input("End: "))

# for count in range (begin, end):
#     if count % 2 == 0:
#         continue
#     print(count)

sum = 0
for count in range(1,100):
    if count % 2 == 0:
        continue
    if count % 3 == 0:
        continue 
    if count % 5 == 0:
        continue
    if count % 7 == 0:
        continue   
    print(count, end = " ")
    sum += count
print()
print("和：",sum)



