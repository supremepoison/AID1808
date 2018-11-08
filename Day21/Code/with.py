



# try:
#     f = open('text.txt', 'w')
#     try:

#         s = int(input('请输入整数:'))

#         f.write('hello')
#     finally:

#         f.close()
# except OSError:
#     print('文件打开失败')
# except:
#     print('读取失败')
#*******************************************
#用with语句实现

try:
   
    with open('text.txt', 'w') as f:

        s = int(input('请输入整数:'))

        f.write('hello')

except OSError:
    print('文件打开失败')
except:
    print('读取失败')