
#*****************************************
##   此示例示意将for用于whi循环中的情况


# for x in range(5):
#     if x == 2:
#         continue
#     print(x)
#*****************************************
# 跳过奇数打印10以内偶数

# for num in range(10):
#     if num % 2 == 1:
#         continue
#     print(num)
#******************************************


# # while continue



# 此示例示意将continue用于whi循环中的情况
# 用while语句打印10以内的偶数

i = 0
while i < 10:
    if i % 2 == 1:
        i +=1
        continue
    print(i)
    i +=1

    