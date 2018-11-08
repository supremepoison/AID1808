
def get_fucntion():
    s = input("请输入您要做的操作：")
    if s =='求最大':
        return max
    if s =='求最小':
        return min
    if s =='求和':
        return sum

L= [2,4,6,8,10]
f = get_fucntion()
print(f(L))
