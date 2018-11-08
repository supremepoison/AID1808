


# def myadd(x, y):
#     return x + y

#可以用lambda改写如下:

# myadd = lambda x,y :x +y
myadd = lambda *args: sum(args)
f1 = lambda : 100+200+320
print(f1())




print("20+30=",myadd(20, 30))
print("100+200=",myadd(100, 200))
