# #练习：
#             写一个程序，任意输入一些整数，当输入小于零的数时结束输入，
#             当输入完成后，打印您输入的这些正整数的和



# s = 0
# while True:
#     a = int(input("Enter numbers:"))
#     s +=a
#     if a < 0:
#         break
# print(s)





i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(i * j ,end = " ")
        j +=1
    print()
    i +=1