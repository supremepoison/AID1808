


def mysum(n):
    if n == 1:
        return 1
    return n + mysum(n-1)
print(mysum(998))

def testage(n):
    if n == 1:
        return 10 
    return 2 + testage(n-1)                                                                                                                                                                                                          
print(testage(5))
