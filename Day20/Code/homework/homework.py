# 2. 自己写一个Mylist类,实现重写len,str
#     让MyList类型的对象变为可迭代对象

#   3. 写一个类Fibonacci实现迭代器协议,此类的对象可以作为可迭代对象生成斐波那契数列
#          1 1 2 3 5 8 13 ....
#     class Fibonacci:
#         def __init__(self, n):
#             ...
#         ...
#     for x in Fibonacci(10):
#         print(x)  # 打印 1 1 2 3 5 8 ...
#     L = [x for x in Fibonacci(50)]
#     print(L)
#     print(sum(Fibonacci(100)))



# class Fibonacci:
#     def __init__(self, n):
#         self.L = [1, 1]
#         self.num = n
#         if n == 1:
#             self.L = [1]
#         elif n == 2:
#             self.L = [1, 1]
#         else:
        
#             for i in range(self.num):
#                 self.L.append(self.L[-1] + self.L[-2])

#     def __iter__(self):
#         return Fibonacci_Iterator(self.L)

# class Fibonacci_Iterator:
#     def __init__(self, data):
#         self.data = data
#         self.current_index = 0

#     def __next__(self):
#         if self.current_index >= len(self.data)-2:
#             raise StopIteration

#         r = self.data[self.current_index]
#         self.current_index += 1
#         return r
#********************************************************        
    

class Fibonacci:
    def __init__(self, n):
        self.count = n
        self.a = 0
        self.b = 1
        self.cur_count = 0    
           
    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_count >= self.count:
            raise StopIteration
        v = self.b
        self.a, self.b = self.b, self.a + self.b
        self.cur_count += 1
        return v 

    
    



for x in Fibonacci(10):
    print(x)  # 打印 1 1 2 3 5 8 ...

# L = [x for x in Fibonacci(50)]
# print(L)
# print(sum(Fibonacci(100)))

