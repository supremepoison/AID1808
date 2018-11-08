#此示例示意文件的读操作

try:

    #打开文件
    f = open('mynote.txt')  #打开文件, 用f绑定文件流对象
   
    print("成功打开文件")
    #读写文件
    s = f.readline()    #从文件中读取一行文字
    print('您读到的是',s)
    print('您读到的字符个数是:',len(s))

    sss= f.read()
    print(sss)


    ss = f.readlines()  #从文件中读取多行文字
    print(ss)

    #关闭文件
    f.close()
    print("成功关闭文件")
except OSError:
    print('打开文件失败')