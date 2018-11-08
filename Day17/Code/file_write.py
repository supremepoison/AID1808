

#此示例示意写文本文件
#1.打开文件
f = open('myfile.txt', 'w')

print('打开文件成功')
#2.写文件
f.write('这是第一行文字')
f.write('\n')
f.write('ABCDEFG')
f.write('\n')

f.writelines(['aaaaaaa', 'bbbbbbbb','ccccccc'])


print('写文件成功')

#3.关闭文件
f.close()
print('关闭文件成功')