
list = []

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

def delete_student():
    n = input("Enter the name:")
    for i in list:
        if i['name'] == n:
            list.remove(i)
            print("delete successfully")
            return list
    else:
            print("nobody")
            
def modify_student():
    n = input("Enter the name :")
    for i in list:
        if i['name'] == n:
            score = input("Enter the new score:")
            i['score'] = score
            print("modify successfully")
            return list
            
    else:
            print("nobody")
