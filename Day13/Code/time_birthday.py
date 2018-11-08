



import time
# a = tuple(input("birthday:"))
b = time.mktime((1996,4,30,20,3,4,0,0,0))
# c = time.mktime((2018,9,18,16,23,0,0,0,0))
c = time.time()
d = (c - b) /60 /60 /24//365
e = time.localtime(830865784)
print(d)
print(e)