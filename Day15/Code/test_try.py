

# def get_score():

#     a = int(input("Enter a number between 0 and 100:"))
#     if not(0 <= a <= 100):
#         return 0
#     return a
# try:
#     score = get_score()
# except ValueError:
#     score = 0
# print("The numbr is ", score)


#函数内部加入try语句来进行错误处理
def get_score():
    try:
        a = int(input("Enter a number between 0 and 100:"))
    except ValueError:
        return 0
    if not(0 <= a <= 100):
        return 0
    return a
print("The number is ", get_score())

    