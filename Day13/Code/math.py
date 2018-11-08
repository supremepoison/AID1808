# 练习
#     1.输入一个圆的半径,打印出这个元的面积
#     2.输入一个元的面积,打印出这个圆的半径

# import math as m
# r = float(input("radius:"))
# area = m.pi * r **2
# print("area:",area)


# area2 = float(input("area:"))
# r2 = m.sqrt(area2/m.pi)
# print("radius", r2)



import math
s= 0
for i in range(1,21):
    s += math.factorial(i)
print(s)
