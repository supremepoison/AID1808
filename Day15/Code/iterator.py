

L = [2, 3, 5, 7]
it = iter(L) #obtain iterator
while True:
    try:
        x = next(it)
        print(x)
    except:
        break