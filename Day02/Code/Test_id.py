#经过优化后，a 和b 可能是同一个值
a =10
b =10
print(id(a))
print(id(b))
print(a is b )