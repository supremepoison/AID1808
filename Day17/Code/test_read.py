

f = open('data.txt')

#方法1, 每次读取一行,然后进行处理后打印
# while True:
#     line = f.readline()
#     if line == '':
#         break
#     line = line.strip() #去掉末尾的'\n'
#     L = line.split()    #将其拆分成列表
#     print('name:', L[0], 'phone number :', L[1])


#方法2,先读取所有文本到内存中,形成列表
# for c in f.readlines():
#     b = c.strip()
#     a = b.split(' ')
#     print('name:',a[0],'number:', a[1])

#方法3, 用read读取数据到内存中,然后再分行处理
s = f.read()
lines = s.split('\n')
for i in lines:
    a = i.split(' ')
    print('name:',a[0],'number:', a[1])

f.close()
    






