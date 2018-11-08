
#  写程序，实现复制文件功能
#     要求:
#       1) 源文件路径和目标文件路径需手动输入
#       2) 要考虑关闭文件问题
#       3) 要考虑超大文件复制问题
#       4) 要能复制二进制文件(如:/usr/bin/python3 等文件)


# source_file = input("Enter the source path:")
# copy_file = input("Enter the copy path:")

# myfile = open(source_file,'rb')
# a = myfile.read()
# # print(a)
# myfile.close()

# cpfile = open(copy_file,'wb')
# b = cpfile.write(a)
# cpfile.flush()
# cpfile.close()

def mycopy(src_file, dst_file):
    ''' 
    此函数共实现复制文件

    '''
    try:
        fr = open(src_file, 'rb')
        try:
            try:

                fw = open(dst_file, 'wb')
                try:
                    while True:
                        data = fr.read(4096)
                        if not data:
                            break
                        fw.write(data)
                except:
                    print('something wrong')
                finally:
                    fw.close()
            except:
                print('open write file failed')
                return False
            
        finally:
            fr.close()
    except:
        print('open read file failed ')
        return False
    return True


s = input("Enter the source path:")
d = input("Enter the target path:")
if mycopy(s,d):
    print('copy successfully')
else:
    print('copy failed')