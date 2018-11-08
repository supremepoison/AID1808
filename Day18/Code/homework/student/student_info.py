
# list = []

def max_min_score():
    L = sorted(list, key = lambda d:d['score'], reverse = True)
    print_student(L)
    return L

def min_max_score():
    L = sorted(list, key = lambda d:d['score'])
    print_student(L)
    return L

 
 
def max_min_age():
    L = sorted(list, key = lambda d:d['age'], reverse = True)
    print_student(L)
    return L

def min_max_age():
    L = sorted(list, key = lambda d:d['age'])
    print_student(L)
    return L

def input_student():
    
    while True:
        d ={}

        n = input("Enter your name('Enter' == quit):")

        if not n:
            break
        while True:
            try:
                a = int(input("Enter your age:"))
            except:
                print("Input Error")
                continue
            else:
                break
        
        while True:
            try:
                s = int(input("Enter you score"))
            except:
                print("Input Error")
                continue
            else:
                break
        
           

        d['name'] = n
        d['age'] = a
        d['score'] = s
        for i in list:
            if n == i['name']:
                print("This name already exists")
                return input_student()
            
        list.append(d)
    return list

    
def print_student(list):
    width = 0
    for y in list:
        

        biggest=len(max(y['name'],str(y['age']),str(y['score']) ))
        if biggest > width:
            width = biggest

        
    print('+'+ '-'*(width+15) + '+' + '-'*(width+15) +'+'+ '-'*(width+15) +'+')

    print('|'+'name'.center(width+15)+ '|'+ str('age').center(width+15)+ '|'+ str('score').center(width+15)+ '|')

    print('+'+ '-'*(width+15) + '+' + '-'*(width+15) +'+'+ '-'*(width+15) +'+')

    for d in list:
        line = '|'+d['name'].center(width+15)+ '|'+ str(d['age']).center(width+15)+ '|'+ str(d['score']).center(width+15)+ '|'
        print(line)
    print('+'+ '-'*(width+15) + '+' + '-'*(width+15) +'+'+ '-'*(width+15) +'+')

def delete_student(list):
    n = input("Enter the name:")
    for i in list:
        if i['name'] == n:
            list.remove(i)
            print("delete successfully")
    # for d , i in enumerate(list):
    #     if n == i['name']:
    #         del list[d]
    #         print("delete successfully")
    #         return list

    else:
            print("nobody")
            
def modify_student(list):

    n = input("Enter the name :")
    for i in list:
        if i['name'] == n:
            score = input("Enter the new score:")
            i['score'] = score
            print("modify successfully")
            return list
            
            
    else:
            print("nobody")

def student_read(list):
    L = []
    try:
        rd = open('/home/tarena/AID1808/Day18/Code/homework/student/si.txt')
        for line in rd:
            line = line.strip()
            items = line.split(',')
            n, a, s = items
            a = int(a)
            s = int(s)
            L.append(dict(name = n, age=a, score = s))
        print('读取成功')
        rd.close()
    except:
        print('读取文件失败')
    return L

def student_write(list):
    try:
        wt = open('/home/tarena/AID1808/Day18/Code/homework/student/si.txt', 'a')
        for d in list:
            wt.write(d['name'])
            wt.write(',')
            wt.write(str(d['age']))
            wt.write(',')
            wt.write(str(d['score']))
            wt.write('\n')


        # for i in list:
        #     wt.write('姓名:%-2s '% i['name'])
        #     wt.write('年龄:%-2s'% str(i['age']))
        #     wt.write('分数:%-2s\n'% str(i['score']))

        wt.close
        print('保存成功')
    except:
        print('保存文件失败')
