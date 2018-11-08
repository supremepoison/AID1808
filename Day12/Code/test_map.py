def power2(x):
    return x**2
# a =0
# for i in map(power2,range(1,10)):
#     a +=i
#     print(a)
# # ********************************************
# m = map(power2, range(1,10))
# print(sum(m))
#****************************
print(sum(map(lambda x:x**3,range(1,10))))










# b= 0
# for i in map(pow, range(1,10), range(9,0,-1)):
#     b +=i
#     print(b)

print(sum(map(pow,range(1,10),range(9,0,-1))))