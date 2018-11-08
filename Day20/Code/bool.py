

class A:
    # def __bool__(self): 
    #     print('__bool__被调用')
    #     return False

    # def __len__(self):
    #     print('__len__方法被调用')
    #     return 0
    

a = A()

print(bool(a))      #True
if a:
    print('a为真值')
else:
    print('a为假值')