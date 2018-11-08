#  练习:(test_sorted.py
#             names = ['Tom', 'Jerryk', 'Spike', 'Tyke']
#             排序的依据是'moT' 'kcaJ'...
#             结果是:
#                 ['Spike', 'Tyke', 'Tom', 'Jerry']


def string(x):
    a =x[::-1]
    print(x,'排序依据',a)
    return a
L = ['Tom', 'Jerry', 'Spike', 'Tyke']

names = sorted(L,key = string)
print(names)