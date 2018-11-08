# def f1():
#     print("hello f1")

# def f2():
#     print("hello f2")

# def fx(fn):
#     print(fn)       #???

#     fn()            # 请问调用谁?
#     print(fn())           


# fx(f1)

def myinput(fn):
    L = [1,3,5,7,9]
    r = fn(L)
   
    return r 

print(myinput(max))
print(myinput(min))
print(myinput(sum))