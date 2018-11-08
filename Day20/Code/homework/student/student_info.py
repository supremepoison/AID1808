
# list = []
from student import Student
def max_min_score(L):
    L1 = sorted(L, key = lambda d : d.get_score(), reverse = True)
   
    
    print_student(L1)

def min_max_score(L):
    L1 = sorted(L, key = lambda d: d.get_score())
   
    
    print_student(L1)

 
 
def max_min_age(L):
    L2 = sorted(L, key = lambda d:d.get_age(), reverse = True)
    
    
    print_student(L2)

def min_max_age(L):
    L2 = sorted(L, key = lambda d:d.get_age())
    
    
    print_student(L2)

def input_student():
    
    L = []
    while True:

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
      
            
        L.append(Student(n, a, s))
    return L

    
def print_student(L):
    width = 0
    for y in L:
        
        n,a,s = y.get_infos_string()
        

        biggest=len(max(n,str(a),str(s) ))
        if biggest > width:
            width = biggest

        
    print('+'+ '-'*(width+15) + '+' + '-'*(width+15) +'+'+ '-'*(width+15) +'+')

    print('|'+'name'.center(width+15)+ '|'+ str('age').center(width+15)+ '|'+ str('score').center(width+15)+ '|')

    print('+'+ '-'*(width+15) + '+' + '-'*(width+15) +'+'+ '-'*(width+15) +'+')

    for d in L:
        n,a,s = d.get_infos_string()
        line = '|'+n.center(width+15)+ '|'+ a.center(width+15)+ '|'+ s.center(width+15)+ '|'
        print(line)
    print('+'+ '-'*(width+15) + '+' + '-'*(width+15) +'+'+ '-'*(width+15) +'+')

def delete_student(L):
    n = input("Enter the name:")
    for i in L:
        
        if i.get_name() == n:
            L.remove(i)
            print("delete successfully")
    # for d , i in enumerate(list):
    #     if n == i['name']:
    #         del list[d]
    #         print("delete successfully")
    #         return list

    else:
            print("nobody")
            
def modify_student(L):

    n = input("Enter the name :")
    for i in L:
        
        if i.get_name() == n:
            score = input("Enter the new score:")
            i.get_score = score
            print("modify successfully")
            return L
            
            
    else:
            print("nobody")

def student_read():
    L = []
    try:
        rd = open('/home/tarena/AID1808/Day19/Code/homework/student/si.txt')
        for line in rd:
            line = line.strip()
            items = line.split(',')
            n, a, s = items
            a = int(a)
            s = int(s)
            L.append(Student(n,a,s))
        print('读取成功')
        print(L)
        rd.close()
    except:
        print('读取文件失败')
    return L

def student_write(list):
    try:
        wt = open('/home/tarena/AID1808/Day19/Code/homework/student/si.txt', 'a')
        for d in list:
            d.write_to_file(wt)

        wt.close
        print('保存成功')
    except:
        print('保存文件失败')
