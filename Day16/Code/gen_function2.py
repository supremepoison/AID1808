# 此示例示意生成器函数的调用顺序


def myyield():
    print("即将生成2")
    yield 2
    print("即将生成3")
    yield 3
    print("即将生成5")
    yield 5
    print("即将生成7")
    yield 7
    print("生成器调用结束")   


gen = myyield() 
it = iter(gen)  # 拿到迭代器时,生成器函数不执行
print(next(it))  #即将生成 2 2
print(next(it))
print(next(it))
print(next(it))
print(next(it))
