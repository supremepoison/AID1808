
#写一个程序，输入一个字符串，如果字符串不是空，则把第一个字符的编码输出

#写一个程序，输入一个整数（0-65535），输出这个值对应的字符




a = input("Input:")
b = ord(a[0])
if a != "":
    print(b)
else:
    print("empty")

c = int(input("Enter 0-65535:"))
print(c, "character:",chr(c))