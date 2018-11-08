# 1.用类来描述一个学生的信息

#     class Student:
#         ...
#     学生信息有:
#         姓名,年龄,成绩
#     将这些学生对象存于列表中,可以任意添加和删除学生信息
#     1)打印出学生的个数
#     2)打印出所有学生的平均成绩
#     3)打印出所有学生的平均年龄
#     (建议用列表的长度来计算学生的个数)
#**************************************************************
#面向过程
# class Student:
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score 
        


# infos = []
# def input_student():
#     L = []
#     while True:
#         n = input('Name:')
#         if not n:
#             break
#         a = int(input('Age:'))
#         s = int(input('Score:'))
#         L.append(Student(n, a, s))
#     return L

# def def_student(L):
#     n = input('Name:')
#     for index, s in enumerate(L):
#         if s.name == n:
#             del L[index]
#             return  

# def get_student_count(L):
#     '打印学生个数'
#     print(len(L))

# def print_avg_score(L):
#     # total_score = sum((s.score for s in L))
#     total_score = 0
#     for s in L:
#         total_score += s.score
#     print('Average:', total_score/len(L))


# infos += input_student()
# print(infos)
# def_student(infos)
# print(infos)

# get_student_count(infos)
# print_avg_score(infos)


# ***********************************************************************************
#面向对象
class Student:
    infos = []
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score 
        

    @classmethod
    def input_student(cls):
        while True:
            n = input('Name:')
            if not n:
                break
            a = int(input('Age:'))
            s = int(input('Score:'))
            cls.infos.append(Student(n, a, s))
        
    @classmethod
    def del_student(cls):
        n = input('Name:')
        for index, s in enumerate(cls.infos):
            if s.name == n:
                del cls.infos[index]
                 
    @classmethod
    def get_student_count(cls):
        '打印学生个数'
        print('Number of people:',len(cls.infos))
    @classmethod
    def print_avg_score(cls):
        # total_score = sum((s.score for s in L))
        total_score = 0
        for s in cls.infos:
            total_score += s.score
        print('Average:', total_score/len(cls.infos))

    @classmethod
    def output_student(cls):
        for s in cls.infos:
            print(s.name, s.age, s.score)


Student.input_student()
Student.output_student()
Student.del_student()
Student.output_student()
Student.get_student_count()
Student.print_avg_score()