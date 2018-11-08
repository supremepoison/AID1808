

#此示例示意用@property 来实现 ,getter setter


# class Student:
#     def __init__(self, s):
#         self.__score = s

#     def get_score(self):
#         return self.__score

#     def set_score(self, s):
#         assert 0 <= s <=100, '成绩超出范围'
#         self.__score = s

#     def __repr__(self):
#         return '%d' % self.__score
        

# s1 = Student(39)
# # print(s1.score)     #取值
# # s1.score = 56465    #赋值

# print(s1.get_score)
# s1.set_score(11)
# print(s1.get_score)


def a():
    L = [1]
    def b():
        global L
        L = [1,2]

 
        return L
    return b()
print(a())


# class Student:
#     def __init__(self, s):
#         self.__score = s

#     @property
#     def score(self):
#         '''getter'''
#         return self.__score
        
#     @score.setter
#     def score(self, s):
#         '''setter'''
#         assert 0 <= s <=100, '成绩超出范围'
#         self.__score = s

#     def __repr__(self):
#         return '%d' % self.__score
        

# s1 = Student(39)
# print(s1.score)     #取值
# s1.score = 5    #赋值
# print(s1.score)     #取值



