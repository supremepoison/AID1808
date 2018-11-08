
#判断x是否为奇数,如果是奇数返回True,否则...

# def isodd(x):
#     return x % 2 ==1

# #生成1-100的奇数
# for x in filter(isodd, range(101)):
#     print(x)

#生成1-100以内的偶数放到列表even中

# even= [x for x in filter(lambda x:x%2==0,range(1,101))]
# print(even)

def isprime(x):
    

    prime = True
    if x < 2:
        prime = False
    else:
        for j in range(2,x):
            if x % j == 0:
                prime = False
    return prime
           
  
Isprime = [i for i in filter(isprime,range(1,100))]
print(Isprime)