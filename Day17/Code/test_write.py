

f = open('infos.txt', 'w')
while True:
    n = input("name:")
    if not n:
        break
    else:
        a = int(input('age:'))
        add = input('address')
        f.writelines([n,',',str(a),',',add,'\n'])
f.close()

myfile = open('infos.txt')

line = myfile.readlines()

for i in line:
    b = i.strip()
    a = b.split(',')
    print('姓名:%s, 年龄:%s, 住址:%s' % (a[0],a[1],a[2]))
myfile.close()
