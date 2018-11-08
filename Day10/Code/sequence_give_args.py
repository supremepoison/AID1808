# 此示例示意序列传参




def myfun1(a,b,c):
    print("the value of a:",a)
    print("the value of b:",b)
    print("the value of c:",c)

s1 = [11,22,33]
myfun1(s1[0],s1[1],s1[2])
myfun1(*s1)     #相当于 myfun1(11,22,33)
s2 = (1,2,'c')
myfun1(*s2)