# 练习:
#         有一个集合:
#             s = {'唐僧', '悟空', '八戒', '沙僧'}
#             用for语句遍历所有元素如下:
#                 for  x in s :
#                     print(x)
#                 else:
#                     print("遍历结束") 
        
#         请将上面的for语句改为为while语句和迭代器实现



s = {'唐僧', '悟空', '八戒', '沙僧'}
i = iter(s)

while True:
    try:
        x = next(i)
        print(x)
    except:

        print("迭代结束+")
        break

