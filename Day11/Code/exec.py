# s= '''v = 100
# def f1():
#     global v
#     v = 200
#     print(v)

# f1()
# print('v=', v)
# '''
# exec(s)

s = "x=100\ny=200\nprint('x+y',x+y)"
exec(s)

x = "print(x+y)\nprint(x*y)"
exec(x,{'x':10, 'y':20}, {'y':2})